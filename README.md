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

## References

- [Anatomy of a matplotlib figure](https://matplotlib.org/gallery/showcase/anatomy.html), [Video](https://www.youtube.com/watch?v=rARMKS8jE9g)
- 
- [Advanced Plots in mpl](http://www.blackarbs.com/blog/advanced-time-series-plots-in-python/1/6/2017)
