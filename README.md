# Jbooks
Jupyter Notebooks for general data science and machine learning efforts (training).

This repository contains a series of Jupyter Notebooks for general Jupyter learning and AI/ML efforts.  Each notebook is numbered stating at 001 progressing numerically as concepts get more involved.  All AI/ML notebooks start with ML_.

If you want to clone this repository and setup the environment yourself please see the instructions for building Anaconda manually.

If you want to use GitHub's Codespaces simply initiate a Codespaces session from the main branch yourself.  Note that there is an assumption of syncing your dotfiles so either fork/clone my configs folder (https://github.com/christophergarthwood/configs) and update your settings (https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account) to point to the cloned configs repository.  By doing this you'll inherit an update to your shell environment that activates and registers anaconda.

You can manually perform this step, see below, if desired.

You will need data to run these notebooks.

# Github Codespaces

Note that due to Cross Origin (CORS) blocks you have to do the following when using Jupyter Notebooks / Lab with Github Codespaces

1.  jupyter lab --ServerApp.disable_check_xsrf=False --ServerApp.allow_origin=\'\*\'
2.  In the Ports section of the interactive portion of Codespaces change the port from Private to Public (this cannot be configured and must be done per session by hand).

# Get the data
Download the tarfile and store it at <root>/data after untarring the file:

https://drive.google.com/file/d/1MdPfxP5s9vrbc0WM79IkpG0alJ00PDLg/view?usp=share_link

# Register the Conda environment manually

conda init bash

# Build the environment using Anaconda manually
conda info --envs                    #shows your environments

conda activate <env_name>            #activates or makes those libs available

conda remove --name <env_name> --all #completly clears the slate and remove that environment

conda create --name machine_learning -y python=3.8 tensorflow tensorflow-datasets tensorflow-gpu jupyter jupyterlab pandas numpy mkl scikit-learn gdal

conda activate machine_learning

conda install imageio seaborn plotly bokeh matplotlib  -y

conda install -c condaforge pathlib netcdf4 nltk wordcloud bs4  -y

conda install -c condaforge proj -y

conda install -c condaforge contextily descartes geopandas cartopy shapely  -y

# Build the environment using Anaconda manually in Codespaces
CONDA_EXE=${which conda}

${CONDA_EXE} activate machine_learning

${CONDA_EXE} create --name machine_learning -y python=3.8 tensorflow tensorflow-datasets tensorflow-gpu jupyter jupyterlab pandas numpy mkl scikit-learn gdal

${CONDA_EXE} install -c conda-forge cartopy -y

${CONDA_EXE} update --all -c conda-foge -y

sudo $(which conda) env export --from-history --name machine_learning > striped.yml

sudo $(which conda) env export --no-builds  --name machine_learning > ./environment/archless_environment.yml 

sudo $(which conda) env export --name machine_learning > ./environment/environment.yml 

sudo $(which conda) env create --prefix /opt/conda/envs/machine_learning/ --file ./environment/archless_environment.yml

# Clean Up the Anaconda release to make disk space
sudo $(which conda) clean --all -y

# References
https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html
