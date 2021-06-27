## Astrolgy Data
Data scraped from [Astro-Databank](https://www.astro.com/astro-databank) for Research.

### Requirements
- Python 3.7
- beautifulsoup4

### Example of a website page and extrated to json
<!-- #### Website page of a data
![Astro Site data example](./demo/astro_site.png)
#### Extracted the website data into json
![Json example](./demo/json.png) -->
<img src="./demo/astro_site.png" width="350"> | <img src="./demo/json.png" width="480">

### How to use the repository
- **full_data.zip** contains all the data available on the site
- For getting the data one by one
  ```
  $ python3 loopAllPage.py
  ```
- For getting the data using multi-threading
  ```
  $ python3 multiprocessAllpage.py

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please cite this repository, if you use in any publications.