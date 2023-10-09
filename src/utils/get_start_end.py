class StartEnd():

    def start(self):
        while True:
            start = input('Define Start: ')
            if start.isdigit():
                return int(start)
            elif (start.startswith('-') and start[1:].isdigit()):
                return int(start)
            else:
                print('invalid input, Try again')
                continue


    def end(self):
        while True:
            end = input('Define End: ')
            if end.isdigit():
                return int(end)
            elif (end.startswith('-') and end[1:].isdigit()):
                return int(end)
            else:
                print('invalid input, Try again')
                continue
