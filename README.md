# Install Dependencies

```bash
conda remove -y -n dataviz --all
conda create -y -n dataviz python=3.6
conda activate dataviz
conda install -y -c conda-forge jupyterlab \
                                altair \
                                seaborn \
                                bqplot \
                                ipywidgets \
                                ipyleaflet \
                                nodejs
jupyter lab clean
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```
