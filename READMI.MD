# Soil Project

Create soil application to learn FastAPI basics

## Introduction & Learning Path 

- Asyncronous vs Synchronous Programming
- ASGI Frameworks (routing, middleware, response)
   Starlette > FastAPI
- FastAPI focus on Validation. Docs and Devolopment process
- Conda Virtual Environtment

## Project run sources

- Install conda & create virtual environtmen 

'''
brew install miniconda
conda --version
conda env list

conda create --name soil python=3.11.0
conda create --name soil python=3.11.0 numpy
conda activate soil
conda deactivate

pip install pillow 
pip freeze > requirements.txt
pip install -r requirements.txt
'''