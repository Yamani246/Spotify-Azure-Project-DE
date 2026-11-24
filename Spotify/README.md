# Spotify Data Engineering – Azure Databricks

This folder contains the Azure Databricks implementation of the Spotify End-to-End Data Engineering project. It handles data ingestion, transformation, data quality, and incremental processing using Apache Spark and Delta Lake.

## Project Overview

The Databricks component follows the **Medallion Architecture**, organizing data into three layers:

- **Bronze Layer:** Stores raw ingested Spotify data.
- **Silver Layer:** Cleans, validates, and transforms the raw data.
- **Gold Layer:** Stores refined, analytics-ready data.

## Technologies Used

- Azure Databricks
- Python and PySpark
- Apache Spark
- Delta Lake
- Azure Data Lake Storage Gen2 (ADLS Gen2)
- Databricks Auto Loader
- Spark Structured Streaming
- Spark Declarative Pipelines
- Delta Lake Change Data Feed / Auto CDC (as implemented)
- Databricks Asset Bundles (DAB)

## Key Implementations

- Built data processing layers using the Medallion Architecture.
- Used PySpark for data cleansing and transformations.
- Implemented incremental file ingestion using Auto Loader.
- Applied data quality expectations to validate incoming records.
- Used streaming pipelines for incremental data processing.
- Implemented CDC processing to manage changes in records.
- Stored processed data in Delta tables.

## Project Structure

```text
Spotify-Databricks/
│
├── jinja/          # Jinja templates
├── resources/      # Databricks job and pipeline configurations
├── src/            # Python source code
├── utils/          # Reusable utility functions
│
├── databricks.yml  # Databricks Asset Bundle configuration
├── pyproject.toml  # Python project dependencies and configuration
├── .gitignore      # Git ignore rules
└── README.md       # Project documentation
```

## Databricks Asset Bundles

This project uses Databricks Asset Bundles to manage and deploy Databricks resources.

### Prerequisites

- Access to an Azure Databricks workspace
- Databricks CLI installed
- Python installed
- Git configured

### Validate the Bundle

```bash
databricks bundle validate -t dev
```

### Deploy to Development

```bash
databricks bundle deploy -t dev
```

### Deploy to Production

```bash
databricks bundle deploy -t prod
```

> Ensure that the production target is configured for the intended production workspace before deploying.

## Related Project

The Azure Data Factory implementation is available in the `Azure-Data-Factory/` folder at the root of this repository.

