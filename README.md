# Jbooks

Jupyter Notebooks for general data science, machine learning efforts (training), and Large Language Model (LLM) work.

This repository contains a series of Jupyter Notebooks for general Jupyter learning and AI/ML efforts.  Each notebook is numbered stating at 001 progressing numerically as concepts get more involved.  All AI/ML notebooks start with ML_.

If you want to clone this repository and setup the environment yourself please see the instructions for building Anaconda manually, although I recommend using the pre-built environment file.

If you want to use GitHub's Codespaces simply initiate a Codespaces session from the main branch yourself.  Note that there is an assumption of syncing your dotfiles so either fork/clone my configs folder (https://github.com/christophergarthwood/configs) and update your settings (https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-github-codespaces-for-your-account) to point to the cloned configs repository.  By doing this you'll inherit an update to your shell environment that activates and registers anaconda.


# Github Codespaces

The entire process is self-contained will build the environment, download the data, and register Anaconda with the environment built for you via the ./script/bootstrap script.

Make sure you source your .bashrc prior to starting with this notebook on the command-line (CLI):

```
source ~/.bashrc;
```

Also ensure, after sourcing your rc file, that you:

```
conda activate machine_learning_gpu;
```

Then in the /workspaces/jbooks folder (which you should default in):

```
./script/run_codespaces_jupyter;
```

Load the resulting web page in your browser, ensuring you copy the session key from the CLI and pasting it into the dialog screen.

Your Jupyter enviroment will start showing in 10-20 seconds.

You will need data to run these notebooks, see the Get the Data section.

# Run the Conda environment manually

```
conda init bash;
source ~/.bashrc;
conda activate machine_learning_gpu;
/workspaces/jbooks/script/run_codespaces_jupyter;
```

# Build the environment using Anaconda manually (maybe on your laptop)

## Shows your environments

```
conda info --envs;
```

## Activates or makes those libs available

```
conda activate machine_learning_gpu;
```


## Completly clears the slate and remove that environment

```
conda remove --name machine_learning_gpu --all;
```

## Starts building the environment

#### Minimal setup (with intent of using GPU, focus is local user installation, Ubuntu 20.04)

```
conda create -n machine_learning_gpu python=3.9;
conda activate machine_learning_gpu;
conda install -c conda-forge cudatoolkit=11.8.0 -y;
pip install nvidia-cudnn-cu11==8.6.0.163 --user;
pip install tensorflow==2.13.1 --user;
pip install tensorrt --user;
```

Ensure you update the LD_LIBRARY_PATH in your `~/.bashrc` to add the new tensorrt and cudnn libs to your setup.

*Example only, your milage may vary.*

```
export LD_LIBRARY_PATH="/usr/lib:/usr/lib64";
export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/lib:/usr/lib64:${PATH_ROOT}/.local/lib/python3.9/site-packages/nvidia/cudnn/lib:${PATH_ROOT}/.local/lib/python3.9/site-packages/tensorrt_libs";
```

#### Additional (required) libraries by category

```
conda activate machine_learning_gpu;
```

*Science Libs*

```
conda install -c conda-forge numpy pandas tabulate scipy matplotlib -y;
```

*Jupyter*

```
conda install -c conda-forge jupyter jupyterlab jupyter_dashboards jupyter_contrib_nbextensions -y;
```

*Progressbar*

```
conda install -c conda-forge nbconvert tqdm -y;
```

*Sci-Kit*

```
conda install -c conda-forge scikit-learn -y;
```

*Tuning*

```
conda install -c conda-forge keras-tuner optuna -y;
```

*Image Processing*

```
conda install -c conda-forge opencv imageio albumentations imgaug -y;
```

*Code Linting*

```
conda install -c conda-forge pylint autopep8 black -y;
```

*OpenAI*

```
conda install -c conda-forge openai -y;
```

*Large Language Model (LLM) Infrastructure*

```
conda install -c conda-forege fire longchain transformers;
```

*Natural Language Processing (NLP)*

```
conda install -c conda-forge pathlib nltk wordcloud bs4 -y;
```

*Pip (Nltk, Graphics Lib, Non-Anaconda, not available via Anaconda)*

```
pip install svgling --user;
```

*Extra tools (NetCDF, Xarray, Logging)*

```
conda install -c conda-forge netCDF4 xarray icecream geopandas;
```

*Plotting Packages and GIS*

```
conda install -c conda-forge cartopy holoviews hvplot bokeh seaborn;
```

***OR use***

# Environment export / creation methods

```
sudo $(which conda) env create --prefix /opt/conda/envs/machine_learning_gpu/ --file ./environment/environment.yml;
```

# Get the data
Download the tarfile and store it at /workspaces/ after untarring the file:

https://drive.google.com/file/d//1vSq-KCfEL_KoxdE4lxeO2rEKU77kiEkR/view?usp=share_link

Create the following directories:

```
mkdir -p /workspaces/tmp;
mkdir -p /workspaces/logs;
mkdir -p /workspaces/data;
```

Then in /workspaces

```
tar xvfz ./data.tgz;
```

which will unpack the data into /workspaces/data.

# To create an environment file:

***Stripped down version of an environment***
```
sudo $(which conda) env export --from-history --name machine_learning_gpu > striped.yml;
```

***Most secure method cross-platform***
```
sudo $(which conda) env export --no-builds  --name machine_learning_gpu > ./environment/archless_environment.yml;
```

***Most generic method***
```
sudo $(which conda) env export --name machine_learning_gpu > ./environment/environment.yml;
```

# Clean Up the Anaconda release to make disk space
```
sudo $(which conda) clean --all -y;
```

# References

## Tensorflow Install Reference
https://cse.ucdenver.edu/~biswasa/posts/2023/08/biswas/blog-ubuntu-tensorflow/

## Cloud Provider CLI commands

### Google Cloud Provider (GDP) - `gcloud`
[gcloud](https://cloud.google.com/storage/docs/gsutil_install#linux)

### Amazon Web Services (AWS) - `aws`
[aws](https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html)

Azure - `az`
[az](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=script)

# Really Useful Notes

## Load new Kernel on the fly (not generic)
```
mamba env create -f /home/jovyan/environment.yml;
echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/jovyan/.bash_profile;
echo "conda deactivate" >> /home/jovyan/.bash_profile;
echo "conda activate <your environment name>" >> /home/jovyan/.bash_profile;
. /opt/conda/etc/profile.d/conda.sh;
conda activate <your environment name>;
python -m ipykernel install --user --name <your environment name>;
source /home/jovyan/.bash_profile;
```

*Your Jupyter enviroment will start showing in 10-20 seconds.*

You will need data to run these notebooks, see the Get the Data section.

## Ubuntu Server (20.4) Install GPU Drivers in general

### Display all available modules. 
```
find /lib/modules/$(uname -r) -type f -name "\*.ko";
```

### Show Hardware
`lshw;`

### Show Video Card
`sudo lshw -c video;`

### See the list of available HW.
`sudo ubuntu-drivers list;`

### See what is actually available.
`sudo apt-get install linux-headers-$(uname -r);`

`sudo apt-key del 7fa2af80;`

`sudo apt install build-essential libglvnd-dev pkg-config;`

*This method worked best and gives you the best possible drive (maybe).*

`sudo ubuntu-drivers install –-gpgpu;`

*Restart the system because the kernel modules for the driver need to be loaded (easiest).*

`sudo reboot now;`

*What version are you using?*

`cat /proc/driver/nvidia/version;`

*Are the kernel modules loaded?*

`lsmod | grep nvidia;`

*This will show you GPU availability.*

`nvidia-smi;`

*Show graphics driver details*

`nvidia-smi --query-gpu=driver_version --format=csv`

### Ubuntu Clean up 
```
sudo rm -rf /etc/modprobe.d/nvidia-graphics-drivers.conf;
sudo update-initramfs -u;
sudo apt remove *nvidia*;
sudo reboot now;
```

=======

#### Example Jupyter Port Forwarding:
`ssh -i ${the_key} -N -L localhost:8080:localhost:8080 ${the_user}@${the_ip}


### Create A GitHub Workflow

+ [Quickstart](https://docs.github.com/en/actions/quickstart)
+ [Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)

# References
+ (Sharing Anaconda Environments)[https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/04-sharing-environments/index.html]
+ (NVIDIA Install Guide)[https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html]
+ (Jupyter Notebook Password Setup / Config)[https://medium.com/@nyghtowl/setup-jupyter-notebook-access-on-google-compute-engine-with-https-ad69297f438b]
