
# Project: 3D Plotting

## Summary of proposal

  
  

### Why this project?

My open-source journey began with SunPy about 4 months ago, I enjoyed having to look at the visualization capabilities of SunPy and developed a keen interest in visualization while exploring the package and attempting to solve its issues. The efficient usage of python and purposeful open source contribution was the main drive for me.

I have worked with Python as my primary programming language for over 3 years now and I have a strong understanding of Python and Pyvista while contributing to SunPy continued to make me better at it.

I have been involved with contributing towards and understanding SunPy with its underlying libraries for about 4 months now which excites and gives me the confidence that I need to be able to complete the given project successfully and according to the required standards.

  

## Project Roadmap

### Synopsis

SunPy has multiple extensive 2D visualization features for plotting Maps. The ability to have to convert these plots into 3D would enhance the capabilities of SunPy visualization.

This project would include adding a separate python package that extends 3D plotting functionality to SunPy, by using **PyVista**. It would also recreate some of the various existing features and overlays that SunPy's GenericMap has in 3D.

The entire project is split into 3 major components which include:-

#### 1) Package Infrastructure
- The entire project will consist of not only writing new code but also working towards combining the entire project into a usable python package that works accurately with SunPy in accordance with the given standards.
- The 3D PFSS field lines from Pfsspy shall also be implemented and tested carefully.
- The underlying packages for 3D plotting would have to be listed out and this has to be carefully tested with different versions of the packages to make sure that this works with SunPy.
- The existing code makes use of PyVista for 3D plotting functionality and all of the code for 3D plotting would make use of PyVista itself. Currently, there exists simple functionality for plotting any given `GenericMap` from SunPy to be plotted using Pyvista and this will be the baseline from where I would pick up from.
- There are no bounds defined for 3D plotting capability and adding extra functionality for plotting Astropy's coordinates shall also be implemented.

  

#### 2) Extensive documentation

- As of SunPy standards, documentation is extremely important. The entire documentation process shall be written using **Sphinx** as SunPy uses the same. I am also well-versed in the same as I have worked with it extensively before.
- Required documentation is a general order from writing the Index file followed by
	- Introduction
	- Installation
	- Description of the package
	- Reference API which includes the class inheritance diagrams and function description required for the code that shall be written
	- Example Gallery
	- Contribution and release history.
- Sphinx's **Autodoc** allows the extensive documentation of classes and functions which makes use of the well-written docstrings in Python to create the required documentation. Therefore relevant docstrings are to be written that highlight the usage of every class and method with its required parameters and function.
- Gallery Examples shall also be written according to the added code depending on how Sphinx interacts with Pyvista.

  

#### 3) Testing and Integration with SunPy and PfssPy

- The entire project shall be tested systematically wherever necessary.
- Testing shall mainly be performed with **Tox**. The project shall be set up using tox according to SunPy's requirements.
- If required, **Pytest** shall also be integrated into tox runs for figure and unit testing.
- To ensure proper integration with SunPy and PfssPy, appropriate tests shall be written for this as well. This will be done in a manner similar to how tests have been written for SunPy. 

## Implementation

I shall go about implementing the aforementioned requirements starting with moving the code to a separate python package. I shall initialize this with a tox environment for testing and immediately start writing the required documentation when new code is added and tested.

Equal importance shall be given to both writing new code and extensively documenting the functionality of this code.

 
## Deliverables

#### Successfully creating a new python package to provide 3D plotting for SunPy

The existing code shall be worked on and improved to meet required standards and the entire project would be of a python package that can be installed and used with SunPy or Pfsspy for the extended 3D plotting functionality.

#### Extending of SunPy's various 2D map plotting functionalities to 3D


Various functions from SunPy's 2D GenericMap shall be implemented in 3D. The method of implementing animators and grids shall also be decided and implemented.
These various methods and many more can be implemented in 3D by either plotting them as separate meshes using Pyvista or by altering the data that is projected by the map.

  

#### Well-written documentation for the written code.

All of the code that already exists and all the new code shall be combined into a package with well-written documentation using **Sphinx**.
Examples of plots shall be generated with a gallery reference in the documentation. All 3D plots shall be rendered in 2D for documentation purposes.

#### Efficient Testing and Integration

All of the newly implemented classes and methods shall be tested. Unit tests and Figure tests shall be written wherever required by using Tox and PyTest. 
The appropriate 3D testing methodology shall also be looked into, researched and decided on.
CircleCI shall also be implemented to handle cloud-based testing.

  
  

### Timeline

___

#### Community Bonding Period

___

  

- I shall focus on getting familiar with the working of Sphinx and producing doctest with Sphinx, PyTest, and Tox.
- Understand the main plot testing methodology. Currently, figure tests are performed through `pytest-mpl`. Either use a different figure testing methodology or test in accordance with the current figure testing method existing in SunPy which will be decided based on input from the mentors.
- The existing code shall also be tested according to the various 3D plots on render. The plots shall be rendered using PyVista's show through Jupyter Notebook with the appropriate `cpos` location so the entire 3D plot is visible clearly from a 2D perspective especially for example plotting and testing.
- I shall also spend time exploring the capabilities of 3D plotting and continuously add functionality such as the extension of plotting to `LASCO maps` and work on the exploration of magnetic field lines from `PfssPy`.

- I shall also familiarise myself with the possibility of extending most of the 2D plotting functionality to 3D from SunPy.

___

#### Coding Period Begins

___

  

#### Week 1

- I shall begin working with the code documentation of the existing code. I am already in the process of writing the docstrings and examples for plotting here;
- Begin with the setting up of documentation via Sphinx and gain information regarding the types of testing that are required;
- I shall also start setting up the project for packaging.

  

#### Week 2

  

- From here I should have a general idea of what to proceed with in terms of extension of the various 2D plotting functionalities into 3D from SunPy.
- I have extended `draw_quadrangle` from SunPy's `GenericMap` to 3D as I had worked on implementing this in 2D for SunPy itself. This method is implemented in accordance with the existing code and can be produced by `plotter.plot_quadrangle(m)`.

  

![draw_quadrangle.png](https://github.com/jeffreypaul15/SunPy3D/blob/master/screenshots/draw_quadrangle.png?raw=true)

- Having understood the testing methodology that is required by now, I shall begin work on implementing the required unit tests for the existing code and I shall give importance to set up the package infrastructure as well in terms of making the new and existing code modular.

  

#### Week 3

  

- The first few days of this week shall go into implementing the tox environment with the set up of PyTest and Tox for unit testing.
- I shall display the required plot from 3D and save this image through `matplotlib` and thereby integrate it with `pytest-mpl`.
- Next, I shall begin work on structuring the appropriate classes for the package as plots from SunPy as well as PfssPy have to be recreated in 3D. This would require writing new code for the appropriate 2D transformations in 3D. Further, some of the extra functionality would have to be vectored into the new package.
- I shall begin work on setting up CircleCI for this project, the configuration files would have to be set up accordingly with Tox and `pytest-mpl`.

  

#### Week 4

- Based on the requirements of the extending 2D plotting functionality to 3D, I shall continue working with adding the existing methods of SunPy's `GenericMap` to 3D and ensure that these extensions are done appropriately with careful comparison from the 2D plots and appropriate tests.
- These plots mainly involve extending functionality from `matplotlib` classes and converting the coordinates to the required units via `SkyCoord` and then converting the appropriate coordinate frame for displaying.
- More research shall be done in terms of grid plotting with `WCS axes` in 3D and also research on `clip_interval` of for `vmin/vmax` set-up of the required 3D plots.

  

#### Week 5

- This entire week I shall ensure that the above listed deliverables from week 1-4 are correctly set up and all of the examples of the newly implemented 3D plots are set up with a gallery to be displayed in the documentation with the appropriate `cpos` argument set when displaying the 3D plot which is rendered in 2D for the example listing.

* All of the written tests up till now are accurate and ensure proper testing of the plots and other methods.

* Ensuring the docstrings of the existing and implemented functions are properly set up for Sphinx's autodoc.

* CircleCI and the tox environment set up should have begun and would continue to set it up according to requirements.

___

#### Phase 1 Evaluation

___

  

#### Week 6 - Week 7

  
- This week I shall begin by writing the documentation of the correctly implemented methods according to the evaluation. I shall set up `Sphinx` and work towards writing clean and efficient documentation.
- The examples of all the created methods shall be loaded into a gallery and using Sphinx and create a `minigallery` for display in the documentation as well.
- The required 3D testing methodology would have been extensively researched upon and a solid conclusion would have to be reached as to how to go about 3D testing with PyVista.
- 
- After basic documentation is set up I shall also allot some time for bugfixes of any major bugs that may arise during the implementation of the 3D plotting as well as the testing and documentation structure.
- I shall also continue setting up CircleCI and have it perform the required tests for this package.
- The number of tests to run shall be decided after discussing with the mentors.
- By now, the bounds of 3D plotting functionality would have certainly increased and I shall continue the step-by-step extension of the 2D plotting functionality to 3D.
- I shall also begin work on adding code for plotting AstroPy coordinate objects.

  
  

#### Week 8

  

- By this week, I shall fully dedicate time to recreate the major 2D plotting functionalities in 3D if not already created. These are the most used ones in SunPy and extra care shall be taken while implementing the basic `GenericMap` extensions if not already implemented by now.
- The tox environment shall be completely set up and all the Pytests shall be integrated accordingly.
- From here I shall set up Sphinx with the themes in accordance with SunPy's standards and conduct a manual test of the documentation of the package so far. I shall continue working on the documentation alongside the code as this would ensure accurate documentation of all the required classes and methods.
- All added code shall be tested on CircleCI to ensure all the tests are passed before merging with the `master` branch of the new package.
- Major bugs (if any) would be resolved by now and a considerable amount of time shall be devoted to testing all of the small implementations.

  

#### Week 9 - Week 10

- I shall use this week to cross-check if all the implemented functionalities are what is required for the project. This will ensure I have worked towards implementing all of required the `sources` from SunPy and overplotting them with the required `field lines` from PfssPy.
- By now all of the required coordinate objects from Astropy and 2D functionality from SunPy shall be properly implemented with the appropriate tests.
- If any new requirements are requested by my mentors, they shall be implemented during these weeks and the testing of the new code will be completed as well.
- The documentation and docstrings shall again be tested with the complete implementation of all the `.rst` files and indexed according to what is required.
- If other tests have to be performed, I shall implement this on `CircleCI` and check for their passing before any merging is done as mentioned before.
- All of the required local tests would have been written by now and I shall also manually check if all the extended methods are tested.
- The entire package would have been set up in PyPi and a few examples would also be listed out here.
___

#### Final Evaluation
Add finishing touches to the aforementioned deliverables and deliver the entire package ready to be used with SunPy.
___

  

## Personal Info
- Time zone: IST (GMT + 5:30)
- Email ID: [jeffrey.paul2000@gmail.com](jeffrey.paul2000@gmail.com)
- GitHub handle: [jeffreypaul15](https://github.com/jeffreypaul15)
- Riot-ID: @jeffreypaul15:matrix.org
- Location: Bangalore, India.

### Education
- University: Dayananda Sagar College of Engineering, Bangalore, India.
- Major: Computer Science, 3rd year.

### Open Source background and Programming experience

  

- Programming Languages: Python, Java, C, JavaScript, Dart (Basic)
- My Contributions to SunPy include 5 merged and 3 WIP repositories and some important ones are :
-  [Added draw_quadrangle method](https://github.com/sunpy/sunpy/pull/4809) [visualization]
-  [Added STEREO/SECCHI client](https://github.com/sunpy/sunpy/pull/4869)
-  [Added dynamic z axis option](https://github.com/sunpy/sunpy/pull/5025) [visualization]
-  [Added tests for map sequence animator](https://github.com/sunpy/sunpy/pull/5041) [visualization]
-  [Added conversion of map data to float64 in GenericMap.rotate()](https://github.com/sunpy/sunpy/pull/5051) [visualization]

I have enjoyed contributing to SunPy and will continue to do so in any event.
Armed with an inclination towards Artificial Intelligence, I have worked as an intern at 3 separate AI-based companies and have worked majorly with Python. 
I have worked with Python as a primary programming language as I have spent over 2 years working, researching, and developing in the field of Artificial Intelligence.
Solar Physics has gained my interest from my contributions to SunPy and from then on I have explored the visualization of SunPy with AstroPy.

## GSoC

  

### Have you participated previously in GSoC? When? Under which project?
No, This is my first time participating in GSoC.


### Are you also applying to other projects?
No, I will only be applying to SunPy.

  

### Commitments

I have college and extra-curricular committments on week days but it takes only about 7-8 hours of my day. Further, my academic load is very less and I will be able to multi-task.
I am open to working full time **~40 hours per week** or more if required.
I do not have any plans for the Summer and I will devote all my time towards GSoc with SunPy.

 
### Eligibility

Yes, I am eligible to receive payments from Google. For any queries, feel free to contact me at jeffrey.paul2000@gmail.com
