# Algorithm-Visualization-GUI
Algorithm Visualization GUI is a Python grapchical user interface that visualizes algorithm stepping through numbers

# Structure
The structure of the project was built using the Model-View-Controller, and Observer design patterns.
The view holds the user interface PyQt5 code, and methods for changing the user interface.  
The view sends triggered events to the controller, and the controller writes to the models.
The models perform logic, and then notify subscribed observers of changes.  
The view recieves the notifications, and makes changes accordinly using its methods.


