Usage
Console works in both interactive and non-iteractive modes.

Command	Example
Run the console:	./console.py (for interactive mode)
Quit the console:	(hbnb) quit
Display the help for a command:		help <command>
Create an object (prints its id):	create <class>
Show an object:		 show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object:	 destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances of a class:	all or (hbnb) all <class>
Update an attribute of an object:	(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update("<id>", "<attribute name>", <attribute value>)


interactive mode:
*example:

$ ./console.py
(hbnb) help
----------------------------------------------------------
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)

---------------------------------------------------------
Non-interactive mode:
*example:

$ echo "help" | ./console.py
---------------------------------------------------------
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
-----------------------------------------------------------------------

