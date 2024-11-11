# FBM-Legalizer
---
## About the project
---
FBM Legalizer is a project based upon the work of Jorge Ferreira, Paulo F. Butzen, Cristina Meinhardt and Ricardo A. L. Reis, as described in their published paper ["FBM: A Simple and Fast Algorithm for Placement
Legalization"](https://ieeexplore.ieee.org/abstract/document/8965013). It is an algorithm aiming to legalize the placement of a standard cell design while maintaining a minimum impact of wirelength and displacement in high-density circuits. This implementation supports designs formulated in the Bookshelf Format.

### Built with
- Python 3.10.12, compatible with any python 3.x.x version.

## Requirements
---
- Python 3.x.x interpreter
- Matplotlib. Used only for visualization purposes by the c_plotter.py. You can install it via a terminal using the command pip3 install matplotlib. (pip3 may be also called as pip depending on the python installations on your system and your OS).
  
## Getting Started
---
- Read/View example.py within the src directory for simple usage example.
- Also check out [Bookshelf Format Parser](https://github.com/PlebeianDev/Bookshelf-Format-Parser) as it is the basis for reading the benchmark designs formulated in the Bookshelf Format. Note that the necessary files of the aforementioned parser are already included in this project.
- The algorithm is implemented in fbm.py file in the src directory and follows the steps as described by the authors. 

## Authors
---
- Original Paper Authors: Jorge Ferreira, Paulo F. Butzen, Cristina Meinhardt and Ricardo A. L. Reis.
- Implementation: George Kranas - [PlebeianDev](https://github.com/PlebeianDev).

## License
---
This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details.

## Acknowledgements
---
Please cite the original authors if you use this project in your work as well as the Parser needed to structure this implementation. 
- Original Paper: [FBM: A Simple and Fast Algorithm for Placement
Legalization](https://ieeexplore.ieee.org/abstract/document/8965013). 
- Parser Paper: [Bookshelf Format Parser](https://ieeexplore.ieee.org/abstract/document/9566264).


## Disclaimer
---
All the information in this repository is provided in good will, for those in need. However I make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability or completeness of any information, and I am not accountable for any misuse (of any kind), of the information provided, by third-parties. Furthermore, I am not the owner of the algorithm implemented in this project, but I am one of the original authors of the parser used to structure the input data for the algorithm.