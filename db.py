import json
import itertools
import pickle


class Table:

    def __init__(self, primaries, commons):

        self.table_primaries = primaries
        self.table_commons = commons
        self.table_headers = self.table_primaries + self.table_commons
        self.storage = {key: {} for key in self.table_headers}
        self.shape = [0, len(self.table_headers)]

    def add_record(self, primaries, commons):
        response = self._check_record(primaries)
        if response == 'ok':  # dict F: first
            values = list(primaries.values()) + list(commons.values())

            for key, value in primaries.items():
                self.storage[key][value] = values

            for key, value in commons.items():
                if self.storage[key].get(value):
                    self.storage[key][value][values[0]] = values
                else:
                    self.storage[key][value] = {values[0]: values}

            self.shape[0] += 1

        return response

    def find_record(self, field, value):

        record = self.storage[field].get(value)
        if record:
            return 'ok', record
        else:
            return 'not found', record

    def edit_record(self, field, value, default_values, new_values):

        response = 'ok'
        changed = self._check_primary_changed(default_values[0], new_values[0])
        if changed:
            response = self._check_record(changed)

        if response == 'ok':
            self.delete_record_by_primary(field, value)
            self.add_record(new_values[0], new_values[1])
        print(response)
        return response

    def delete_record_by_primary(self, field, value):
        response, record = self.find_record(field, value)
        if response == 'ok':
            for key, value in zip(self.table_headers, record):
                if key in self.table_primaries:
                    del self.storage[key][value]
                else:
                    del self.storage[key][value][record[0]]

                    if not self.storage[key][value]:
                        del self.storage[key][value]

            self.shape[0] -= 1

    def delete_record_by_common(self, field, value):
        response, record = self.find_record(field, value)
        if response == 'ok':

            records = list(record.keys())
            for record in records:
                self.delete_record_by_primary(self.table_primaries[0], record)

    def drop(self, field, value):
        if field in self.table_primaries:
            self.delete_record_by_primary(field, value)
        else:
            self.delete_record_by_common(field, value)

    def _check_record(self, pkeys):
        for key, value in pkeys.items():
            if key in self.table_primaries and self.storage[key].get(value) is not None:
                print(key, value)
                return f'primary key "{key}" with value "{value}" already exists'

        return 'ok'

    def _check_primary_changed(self, default_pkeys, new_pkeys):
        changed = {}
        for key in default_pkeys:
            if default_pkeys[key] != new_pkeys[key]:
                changed[key] = new_pkeys[key]
        return changed


if __name__ == "__main__":

    t = Table(['P1'], ['C1', 'C2', 'C3'])

    t.add_record({
        'P1': 'first',
    },
        {
        'C1': 1,
        'C2': 2,
        'C3': 3
    })

    t.add_record({
        'P1': 'second',
    },
        {
        'C1': 1,
        'C2': 2,
        'C3': 3
    })

   # t.edit_record('F', 'first1', [1, 2, 3, 4, 5])

    print(t.find_record('P1', 'first'))
    t.delete_record_by_common('C1', 1)
    print(t.find_record('P1', 'first'))
    print(1)
