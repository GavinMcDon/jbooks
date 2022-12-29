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

`conda install -c condaforge pathlib netcdf4 nltk wordcloud bs4  -y`

`conda install -c condaforge proj -y`

`conda install -c condaforge contextily descartes geopandas cartopy shapely  -y`

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

# Create A GitHub Workflow

+ https://docs.github.com/en/actions/quickstart
+ https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

# References
https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html

