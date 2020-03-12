from PyQt5 import QtCore
import pickle


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, filepath):
        super(TableModel, self).__init__()
        self.filepath = filepath
        self._table = self.import_table(self.filepath)
        self._data_view = self.get_data_view()
        self._search_data = []
        self.search = 0
        self.search_key = None
        self.search_value = None
        self._headers = self._table.table_headers

    @property
    def _index(self):

        data = self.get_data()

        return list(range(1, len(data) + 1))

    def data(self, index, role=QtCore.Qt.DisplayRole):
        data = self.get_data()

        if role == QtCore.Qt.DisplayRole:
            if data:
                value = data[index.row()][index.column()]
                return str(value)

    def get_data(self):
        if not self.search:
            data = self._data_view
        else:
            data = self._search_data

        data.sort()

        return data

    def rowCount(self, parent=None):
        if not self.search:
            return len(self._data_view)
        else:
            return len(self._search_data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return str(self._headers[section])
            if orientation == QtCore.Qt.Vertical:
                return str(self._index[section])

    def add_record(self, data):
        response = self._table.add_record(data[0], data[1])

        if response != 'ok':
            return response

        key, value = list(data[0].items())[0]
        new_record = self._table.find_record(key, value)[1]

        self._data_view.append(new_record)

        self.refresh_data(self.get_primaries()[0], value)

        self._index

        TableModel.save_obj(self.filepath, self._table)

        self.layoutChanged.emit()

        return response

    def add_search_data(self, key, value):

        response, data = self.get_search_data(key, value)
        if response == 'ok':
            self._search_data = data
            self.search_key = key
            self.search_value = value
            self.search = 1

            self.layoutChanged.emit()
        return response

    def delete_record(self, value):

        self._table.delete_record_by_primary(self.get_primaries()[0], value)
        self.refresh_data(self.get_primaries()[0], value)

        self._index

        TableModel.save_obj(self.filepath, self._table)

        self.layoutChanged.emit()

    def edit_record(self, value, default_data, new_data):
        response = self._table.edit_record(self.get_primaries()[0],
                                           value, default_data, new_data)

        if response == 'ok':
            self.refresh_data(self.get_primaries()[0], value)

            self._index

            TableModel.save_obj(self.filepath, self._table)

            self.layoutChanged.emit()

        return response

    def get_headers(self):
        return self._headers

    def get_primaries(self):
        return self._table.table_primaries

    def get_commons(self):
        return self._table.table_commons

    def import_table(self, filepath):
        with open(filepath, 'rb') as file:
            _table = pickle.load(file)

        return _table

    @staticmethod
    def save_obj(filepath, data):
        with open(filepath, 'wb') as file:
            pickle.dump(data, file)

    def get_data_view(self):

        key = self._table.table_primaries[0]

        return list(self._table.storage[key].values())

    def get_dv(self):
        return self._data_view

    def get_search_data(self, key, value):

        response, data = self._table.find_record(key, value)
        if response == 'ok':
            if isinstance(data, list):
                data = [data]
            else:
                data = list(data.values())
        else:
            data = []

        return response, data

    def refresh_data(self, key, value):

        if self.search:
            data = self.get_search_data(
                self.search_key, self.search_value)[1]
            self._search_data = data

        self._data_view = self.get_data_view()

    def reset(self):

        self.search = 0
        self.search_key = None
        self.search_value = None

        self.layoutChanged.emit()
