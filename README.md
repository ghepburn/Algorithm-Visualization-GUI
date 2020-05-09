# Algorithm-Visualization-GUI
PyQt5 single-page interface which steps through chosen algorithms. Built using model-view-controller and observation design patterns. Code focused on OOP. 

The structure of the project was built using the Model-View-Controller, and Observer design patterns.
The view holds the user interface PyQt5 code and methods for changing the user interface.  
The view sends triggered events to the controller, and the controller writes to the models.
The models perform logic, and then notify subscribed observers of changes.  
The view receives the notifications and makes changes accordingly using its methods.


