# Jbooks

Jupyter Notebooks for general data science and machine learning efforts (training).

This repository contains a series of Jupyter Notebooks for general Jupyter learning and AI/ML efforts.  Each notebook is numbered stating at 001 progressing numerically as concepts get more involved.  All AI/ML notebooks start with ML_.

If you want to clone this repository and setup the environment yourself please see the instructions for building Anaconda manually, although I recommend using the pre-built environment file.

If you want to use GitHub's Codespaces simply initiate a Codespaces session from the main branch yourself.  Note that there is an assumption of syncing your dotfiles so either fork/clone my configs folder (https://github.com/christophergarthwood/configs) and update your settings (https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account) to point to the cloned configs repository.  By doing this you'll inherit an update to your shell environment that activates and registers anaconda.


# Github Codespaces

The entire process is self-contained will build the environment, download the data, and register Anaconda with the environment built for you via the ./script/bootstrap script.

Make sure you source your .bashrc prior to starting with this notebook on the command-line (CLI):

`source ~/.bashrc`

Also ensure, after sourcing your rc file, that you:

`conda activate machine_learning`

Then in the /workspaces/jbooks folder (which you should default in):

`./script/run_codespaces_jupyter`

Load the resulting web page in your browser, ensuring you copy the session key from the CLI and pasting it into the dialog screen.

Your Jupyter enviroment will start showing in 10-20 seconds.

You will need data to run these notebooks, see the Get the Data section.



# Build the environment using Anaconda manually (maybe on your laptop)

## Shows your environments

`conda info --envs` 

## Activates or makes those libs available

`conda activate machine_learning`


## Completly clears the slate and remove that environment

`conda remove --name machine_learning --all` 

## Starts building the environment

`conda create --name machine_learning -y python=3.9 tensorflow tensorflow-datasets tensorflow-gpu jupyter jupyterlab pandas numpy mkl scikit-learn gdal`

`conda activate machine_learning`

`conda install imageio seaborn plotly bokeh matplotlib  -y`

`conda install -c conda-forge pathlib netcdf4 nltk wordcloud bs4  -y`

`conda install -c conda-forge proj -y`

`conda install -c conda-forge contextily descartes geopandas cartopy shapely  -y`

# Build the environment using Anaconda manually in Codespaces

`CONDA_EXE=${which conda}`

`${CONDA_EXE} activate machine_learning`

`${CONDA_EXE} create --name machine_learning -y python=3.9 tensorflow tensorflow-datasets tensorflow-gpu jupyter jupyterlab pandas numpy mkl scikit-learn gdal`

`${CONDA_EXE} install -c conda-forge cartopy -y`

`${CONDA_EXE} update --all -c conda-foge -y`

***OR use***

# Environment export / creation methods

`sudo $(which conda) env create --prefix /opt/conda/envs/machine_learning/ --file ./environment/archless_environment.yml`


# Get the data
Download the tarfile and store it at /workspaces/ after untarring the file:

https://drive.google.com/file/d//1vSq-KCfEL_KoxdE4lxeO2rEKU77kiEkR/view?usp=share_link

Create the following directories:

+ mkdir -p /workspaces/tmp

+ mkdir -p /workspaces/logs

+ mkdir -p /workspaces/data

Then in /workspaces

`tar xvfz ./data.tgz`

which will unpack the data into /workspaces/data.

# Register the Conda environment manually

`conda init bash`

`source ~/.bashrc`

`conda activate machine_learning`

`/workspaces/jbooks/script/run_*_jupyter`

# To create an environment file:

***Stripped down version of an environment***

`sudo $(which conda) env export --from-history --name machine_learning > striped.yml`

***Most secure method cross-platform***

`sudo $(which conda) env export --no-builds  --name machine_learning > ./environment/archless_environment.yml`

***Most generic method***

`sudo $(which conda) env export --name machine_learning > ./environment/environment.yml`


# Clean Up the Anaconda release to make disk space
sudo $(which conda) clean --all -y

# Cloud Provider CLI commands

Google Cloud Provider (GDP) - `gcloud`

Amazon Web Services (AWS) - `aws`

Azure - `az`

# Load new Kernel on the fly

+ mamba env create -f /home/jovyan/environment.yml

+ echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/jovyan/.bash_profile

+ echo "conda deactivate" >> /home/jovyan/.bash_profile

+ echo "conda activate <your environment name>" >> /home/jovyan/.bash_profile

+ . /opt/conda/etc/profile.d/conda.sh

+ conda activate <your environment name>

+ python -m ipykernel install --user --name <your environment name>

+ source /home/jovyan/.bash_profile

Your Jupyter enviroment will start showing in 10-20 seconds.

You will need data to run these notebooks, see the Get the Data section.

# Ubuntu Server Install GPU Drivers

+ `find /lib/modules/$(uname -r) -type f -name '*.ko'`
    + Display all available modules. 

+ `lshw`
+ `sudo lshw -c video`
    + See the list of available HW.
+ `sudo ubuntu-drivers list`
    + See what is actually available.
+ `sudo apt-get install linux-headers-$(uname -r)`
+ `sudo apt-key del 7fa2af80`
+ `sudo apt install build-essential libglvnd-dev pkg-config`
+ `sudo ubuntu-drivers install –-gpgpu`
    + This method worked best and gives you the best possible drive (maybe).
#  + `sudo apt-get install cuda-drivers-535`
#  + `sudo apt-get install nvidia-kernel-open-535`
#  + `sudo apt install nvidia-utils-535-server`
#  + Install utility tools like `nvidia-smi`
+ `sudo ubuntu-drivers list`
    + See what actually got installed.
+ `sudo ubuntu-drivers install --gpgpu`
    + This method worked best and gives you the best possible drive.
+ `sudo reboot now`
    + Restart the system because the kernel modules for the driver need to be loaded (easiest).
+ `cat /proc/driver/nvidia/version`
    + What version are you using?
+ `lsmod | grep nvidia`
    + Are the kernel modules loaded?
+ `nvidia-smi`
    + This will show you GPU availability.
=======

ssh -i ~/Downloads/API_KEYs/comm-aai-ssh-key.pem -N -L localhost:8080:localhost:8080 fsclouduser@172.178.50.60


# Ubuntu Clean up 
+ `sudo rm -rf /etc/modprobe.d/nvidia-graphics-drivers.conf`
+ `sudo update-initramfs -u`
+ `sudo apt remove *nvidia*`
+ `sudo reboot now`

# Create A GitHub Workflow

+ https://docs.github.com/en/actions/quickstart
+ https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

# References
+ https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html
+ https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

+ Setup Jupyter with Password and configuration settings
  + https://medium.com/@nyghtowl/setup-jupyter-notebook-access-on-google-compute-engine-with-https-ad69297f438b
