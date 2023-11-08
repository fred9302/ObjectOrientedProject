# Feedback for workshop 1

- Think about which objects/classes should have which responsibilities.
- The Data object should probably not be placed where it currently is in the domain model. Instead it might be a part of the simulator. It should also be more specific.
- GUI should probably be an association to Simulation, instead of being "has\-a"
- Consider where we want to store the data.
  - Should the GUI be in charge of this or should each individual IoT\-node be in charge of it.
  
<img src="./Server client architecture.jpg"   width="700px"   title="Server client architecture" style="object-fit:cover"/>

