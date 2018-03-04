class BankOCR(object):

    PATTERNS = {
        0: [' _ ',
            '| |',
            '|_|',
            '   '],
        1: ['   ',
            '  |',
            '  |',
            '   '],
        2: [' _ ',
            ' _|',
            '|_ ',
            '   '],
        3: [' _ ',
            ' _|',
            ' _|',
            '   '],
        4: ['   ',
            '|_|',
            '  |',
            '   '],
        5: [' _ ',
            '|_ ',
            ' _|',
            '   '],
        6: [' _ ',
            '|_ ',
            '|_|',
            '   '],
        7: [' _ ',
            '  |',
            '  |',
            '   '],
        8: [' _ ',
            '|_|',
            '|_|',
            '   '],
        9: [' _ ',
            '|_|',
            ' _|',
            '   ']
    }

    def convert(self, text):
        entries = []
        lines = text.split('\n')
        for entry_number in range(0, len(lines)-1, 4):
            entry = ''
            for entry_line in range(0, 4):
                entry += lines[entry_number + entry_line] + '\n'
            entries.append(entry)

        return '\n'.join(map(self._x, entries))

    def _y(self, pattern):
        for digit in self.PATTERNS:
            if ''.join(self.PATTERNS[digit]) == pattern:
                return str(digit)
        return '?'

    def _x(self, entry):
        patterns = []
        lines = entry.split('\n')
        for pattern_number in range(0, len(lines[0]), 3):
            pattern = ''
            for line_number in range(0, len(lines)):
                line = lines[line_number]

                pattern += line[pattern_number: pattern_number + 3]
            patterns.append(pattern)
        account_number = ''.join(map(self._y, patterns))

        try:
            account_number.index('?')
            return '{} ILL'.format(account_number)
        except:
            if not self.is_valid(account_number):
                return '{} ERR'.format(account_number)

        return account_number

    def is_valid(self, account_number):
        digits = list(account_number)
        account_sum = 0
        if len(digits) == 9:
            for i in range(0, 9):
                account_sum += (9 - i) * int(digits[i])

            return account_sum % 11 == 0
        return False

