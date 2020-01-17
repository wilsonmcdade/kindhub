"""
Config parser for kindhub
Author: Wilson McDade
"""

from app import Widget

def find_next_widget(line,file):
    
    for line in file:
        if line != "\n":
            pass
        else:
            parser(line,file)

def gather_config(line,file):
    
    config = []
    config.append(line)
    
    for line in file:
        if line != "\n":
            return config
        elif line[0] == #
            pass
        else:
            config.append(line.split())
    
def parser(line, file):
    
    name = ""
    strname = ""

    for line in file:
        
        if line[0] == "#":
            pass
        elif line[0] == "\n":
            next = find_next_widget(line,file)
            pass

        line_split = line.split()
        
        if line_split[0][0] == "[":
            # line is the name of the widget
            name = line_split[0][1:-1]
        elif line_split[0] == "enabled":
            if line_split[1] == "true":
                # widget is enabled
                print("Widget "+name+" is enabled")
                pass
            else:
                # widget is not enabled
                print("Widget "+name+" is not enabled")
                next = find_next_widget(line,file)
        elif line_split[0] == "strname":
            strname = line[1]
        elif line_split[0] == "route":
            route = line_split[1]
        else: 
            config = gather_config(line,file)
    return Widget(name=name,route=route,strname=strname,config=config,next=find_next_widget(line,file))

def config_reader(filename):
    with open(filename) as file:
        for line in file:
            if line[0] == "#" or line[0] == "\n":
                pass
            else:
                parser(line,file)
