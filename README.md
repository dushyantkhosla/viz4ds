## Interactive Data Visualization

This repo has tools and examples showing how to create Interactive Data Visualizations in Python using

- pandas
- seaborn
- altair
- bqplot
- ... and more

## Dependencies

- Use the `/docker` folder to create a container, or 
- Use a Conda env

```bash
conda remove -y -n dataviz --all
conda create -y -n dataviz python=3.6
conda activate dataviz
conda install -y -c conda-forge jupyterlab \
                                altair \
                                vega_datasets \
                                seaborn \
                                bqplot \
                                ipywidgets \
                                ipyleaflet \
                                nodejs
jupyter lab clean
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install bqplot
```
