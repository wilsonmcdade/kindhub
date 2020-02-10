'''
Wilson's Config Reader
Built for github.com/wilsonmcdade/website
Modified for kindhub
Author: Wilson McDade / wilsonmcdade@github
'''

def reader(filename):
    """
    Reads the file, splits the line, then calls parser to append to a list of widgets if needed.
    @param filename: config file as string
    """
    widgets = {}
    file = open(filename)

    for line in file:
        split = line.split()
        if line[0] == '*':
            file.close()
            return widgets
        elif len(split) < 1:
            pass
        elif split[0][0] == '[':
            widg = parser(line,file)
            widgets[widg['name']] = widg
        else:
            pass
    file.close()
    return widgets

def parser(o_line,file):
    """
    Parses config file. 
    @param o_line: last line read by previous function.
    @param file: opened file
    """
    widget = {}

    name = str
    route = str
    dispname = str
    config = []
    enabled = str

    for line in file:

        if line == '\n':
            break

        clean_line = line.strip()
        split = clean_line.split()
        if len(split) > 1:
            synt = split[0]
            rest = clean_line[len(split[0])+1:]
        else:
            print('No attribute. Skipping line.')
            print(line)
            continue

        if line[0] != '#':

            if o_line[0] == '[':
                name = o_line[1:-2]
                widget['name'] = name

            syntax = {
                'enabled:':'enabled',
                'dispname:':'dispname',
                'route:':'route'
                }

            if synt in syntax:

                cmd = syntax[synt]
                widget[cmd] = rest

            else:
                widget[synt[:-1]] = rest
                #print(synt,line,syntax)
                pass

    # validation
    if widget['enabled'] != 'true' and widget['enabled'] != 'false':
        print('invalid config')

    return widget

if __name__ == '__main__':
    """
    This is a testing function to check that it is reading the widget correctly.
    """
    reader('config.conf')
    #print(reader('config.conf'))
