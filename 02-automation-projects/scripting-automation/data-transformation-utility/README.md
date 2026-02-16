# KML Polygon Coordinate Extractor

## Overview
A minimal C++ utility developed to extract polygon coordinates from large KML files.  
The tool identifies the `<coordinates>` block within a KML structure and outputs the coordinate pairs in a clean text format.  
It was designed to streamline geospatial preprocessing tasks for neighborhood and zoning datasets from various regions in Colombia.

## Year
2019–2020 (approx.)

## Author
Amílcar Rodríguez

## Technologies
- C++  
- File I/O  
- Text parsing (KML/XML)

## Purpose
This tool automates a previously manual process of locating and extracting polygon geometry from complex KML files.  
The resulting coordinate lists were used for mapping, analysis, and dataset documentation across multiple regional projects.

## How It Works
1. The program reads the full KML file as raw text.  
2. It searches for the polygon’s `<coordinates>` section.  
3. All coordinate pairs inside that block are extracted.  
4. The tool writes them into a simplified `.txt` file, using `/` as a separator.

**Note:**  
The tool extracts **only polygon coordinates**, not metadata fields such as neighborhood names or areas.

## Example Output
```
-75.508138543464284,6.34257538045477/-75.508158932599855,6.342180881656312/...
```

## Sample Files Included
- `OJO_ARCHIVO_COMPLETO_OJO.txt` — Example KML input  
- `EL_RECREO.txt` — Extracted polygon coordinates  
- `CRISTO_REY.txt` — Extracted polygon coordinates  
- `EL_PORVENIR.txt` — Extracted polygon coordinates  

## Notes
This utility was created for internal use and served as a precursor to more advanced geospatial automation tools.  
A future version could extend functionality to export GeoJSON or extract additional attributes.
