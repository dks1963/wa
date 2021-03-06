# Water Accounting Plus Toolbox  ![](figs/wa_logo.png) 

_Independent estimates of water flows, fluxes, stocks, consumption, and services_

---

## <a name="About WA+"></a>About WA+

[Water Accounting Plus](http://wateraccounting.org/index.html) is the process of communicating water resources related information and the services generated from consumptive use in a geographical domain, such as a river basin, a country or a land use class; to users such as policy makers, water authorities, managers, etc.

---

## <a name="Installation"></a>Installation

There are several packages available, which include python. The WA+ team recommends to download the python package of Anaconda. The great advantage of using the standard Anaconda package is that most of the commonly used modules are included in the package. Alternatively, these modules can be installed separately by the user if a different package than Anaconda is preferred.

### <a name="Install Anaconda"></a>Install Anaconda

Anaconda can be downloaded from: [http://continuum.io/downloads](http://continuum.io/downloads). It is recommended to download  the 64 bits version, because this will increase the calculation capacity enormously. However, be sure that your computer/laptop is a 64 bits computer/laptop. 

The WA+ python codes are made for python version 2.7 for Windows operating systems. It is therefore necessary to download this version of python for running WA+ tools. Major changes are made to the python codes and functions if you compare 2.7 with 3+ versions. It is therefore not possible to run WA+ code in python 3+ versions without making some changes to the code.

![](figs/anaconda_install.png) 

After downloading Anaconda you can run the installation of Anaconda by double-click the executable file and follow the automatic installation steps. Choose a logical location for the installation, a logical location is a directory without spaces and preferably near the root folder (C: or D:). In the remaining of this document this directory will be called $HOME. 
The Anaconda package also includes Spyder, which is the IDE (Integrated Development Environment). This is a layout for writing and running python scripts.

### <a name="Install Water Accounting Toolbox"></a>Install Water Accounting Toolbox

The latest Water Accounting Toolbox can be downloaded from the Water Accounting Plus [Github] (www.github.com/wateraccounting/wa) Account (www.github.com/wateraccounting/wa). Click on the "Clone or download" button located on the top right of the window:

![](figs/wa_clone.png) 

After downloading, subtract the data and change the name from "wa-master" into "wa". Copy and paste the complete "wa" folder in the site-packages location of Anaconda ($HOME/Anaconda2/Lib/site-packages). 

### <a name="Install necessary executables"></a>Install necessary executables

In order to run all the Water Accounting Toolbox functions, there are some necessary executables for running the WA+ scripts properly. It is necessary to install the following programs:
- **GDAL:** site: [http://www.gisinternals.com/release.php](http://www.gisinternals.com/release.php) (See also Install GDAL section of this document)
- **7-zip:** site: [http://www.7-zip.org/download.html](http://www.7-zip.org/download.html) (choose: Type = .exe)
- **ImageMagick:** site: [http://www.imagemagick.org/download/binaries/](http://www.imagemagick.org/download/binaries/) (Version: ImageMagick-6.9.7-6-Q8-x64-dll.exe)

This will install the following required executables: 
- **GDAL:** gdal_translate.exe, gdalwarp.exe, gdalbuildvrt.exe, etc.
- **7-zip:** 7z.exe
- **ImageMagick:** convert.exe

Check if the 7z.exe can be found by the computer after installing. This can be done by typing "7z" in the command prompt.
If the executable can not be found, the following message will be shown:

>'7z' is not recognized as an internal or external command. 
>operable program or batch file.

This means that you need to add the directory where the 7z.exe is located to the "Path" environment variables. The way to do this is explained in the Add environment variables section of this manual.

### <a name="Install GDAL"></a>Install GDAL

Open python in your command prompt by typing "python" in order to find the used python version. The version in picture below is "MSC v.1500 64 bit (AMD64)"

![](figs/find_python_version.png)

If you know the version, go to [http://www.gisinternals.com/release.php](http://www.gisinternals.com/release.php) and open the tab corresponding to your python version (for picture: release-1500-x64-gdal-2-1-3-mapserver-7-0-4). 

Download the GDAL core components (gdal-201-1500-x64-core.msi) and the python bindings (GDAL-2.1.3.win-amd64-py2.7.msi). Install the core component first and hereafter the python bindings. Now you will find the GDAL folder in your Program Files.

Set one environment variables:

User variables:
GDAL_DATA >> $HOME/Program Files/GDAL/gdal_data

To add an environment variable see next section.

### <a name="Add environment variable"></a>Add environment variable

To add an environment variable, you need to go to the environment variables manager of your computer. For an Windows 7 system go to: 
Control panel > System and security > System > Advanced system settings > Advanced > Environment variables. 
This will pops up the window as shown below.

![](figs/environment_variables.png) 

If an executable cannot be found by the computer, you need to add a directory in the "Path" environment variable. This can be done by clicking on the "Edit" button when the "Path" variable under the system variables box was selected. Add the directory where the executables are located and make sure that you do not remove the original paths in the "Path" environment. You need to separate the paths with a semi-colon (;) sign.

![](figs/edit_system_variables.png)

### <a name="Create WA environment variable"></a>Create WA environment variable

For the WA Toolbox two environment variables needs to be created. This can be done in the environment variables manager and click on "New.." (see figure below).

![](figs/environment_variables_new.png) 

The environment variables that must be created are:

WA_PATHS >> $HOME/Program Files/GDAL

WA_HOME >> $HOME/Anaconda2/Lib/site-packages

### <a name="How to install all the necessary Python modules"></a>How to install all the necessary Python modules

Modules are tools that can be imported into your python code. They usually contain stand-alone functions, which can be used within your own python code.

In order to import the Water Accounting Toolbox all the modules must be present. This can be checked by running the following line in Spyder:

>import wa

If you get no command everything is fine, else you will see:

>ImportError: No module named ... module name ...

Any missing modules can be installed by using one of the following four methods. 

#### <a name="Method 1"></a>Method 1

If a package is missing, you can search in the anaconda library by starting the command prompt and type:  

>conda install ... module name ...

This will only work if Anaconda is installed. Below is an example of a command to install the "gdal" module by using the Anaconda libary:

![](figs/module_install1.png) 

#### <a name="Method 2"></a>Method 2

You can also use the following command in the command prompt to install a module:

>pip install ... module name ...

Below is an example of a command to install the "pyproj" module by using the pip libary:

![](figs/module_install2.png) 

#### <a name="Method 3"></a>Method 3

It is also possible to install a module by using a .whl file (wheel-file). The wheels can be downloaded here: [http://pythonwheels.com/](http://pythonwheels.com/) and [http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/). Select the wheel containing win32 within the name if a 32 bits version of Python is used, and win_amd64 if the 64 bits version is used. After downloading the module wheel file, open command prompt and change the directory to the directory where the .whl file is located. You can change the directory in command prompt by using the cd command, as shown in the example below. 

![](figs/module_install3.png) 

After changing the directory, use the following command within the command prompt to install the module.

>pip install ... name.whl ... 

#### <a name="Method 4"></a>Method 4

If a module consists of a complete folder with a setup.py script inside after unzipping, the module can be installed by opening the command prompt and change the directory ("cd" command) to the path where the setup.py is located. Then you can install the module by using the following command within the command prompt:

>python setup.py install

---

## <a name="Functions"></a>Functions


---

## <a name="Troubleshoot"></a>Troubleshoot

jpeg2000 library missing (gebruik niet de gdal functies in anaconda omdat deze library hierin mist)
datum.csv  (gdal_data toevoegen)


---

>>>>>>> origin/master
