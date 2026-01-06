# from setuptools import setup, find_packages

# setup(
#     name="src",
#     version="0.0.1",
#     author="Roman Nihal",
#     author_email="nihalroman7@gmail.com",
#     packages=find_packages()
# )


"""
NOTE ABOUT THIS FILE AND PROJECT STRUCTURE

1. Purpose of setup.py:
   - This setup.py exists only for legacy/compatibility purposes.
   - Modern Python packaging, especially with `uv` (PEP 517/518-compliant), uses 
     pyproject.toml as the single source of truth for:
       - Project metadata (name, version, description, authors)
       - Dependencies
       - Build system configuration
   - Editable installs (pip install -e .) are unnecessary because `uv run` automatically 
     exposes the project for imports without installing it.
   - Keeping setup.py alongside pyproject.toml can sometimes cause confusion or conflicts.
     It is retained here only for reference.

2. Best practices for future projects:
   - Avoid naming the project 'src'; 'src' is a folder layout convention, not a project name.
   - Use a descriptive project/distribution name, e.g., 'ete-ml-project'.
   - Keep the importable package namespace separate from the distribution name:
         src/
             ete_ml_project/
                 __init__.py
   - This prevents self-dependency errors, editable install conflicts, and tooling issues.
   - Imports in code should be absolute starting from the package:
         from src.components.data_ingestion import DataIngestion
   - Do not rely on pip install -e . for development; use `uv run` to execute and test code.

3. pyproject.toml best practices:
   - [project.dependencies] should be the single source of truth for all dependencies.
   - [tool.setuptools] should be clean and specify package discovery with:
         packages = { find = { where = ["."] } }
   - Avoid [tool.setuptools.dynamic] pointing to requirements.txt; it conflicts with [project.dependencies].
   - Keep requirements.txt optional and for reference only.

4. Old pyproject.toml configuration (for reference):
   # [project]
   # name = "src"
   # version = "0.0.1"
   # dependencies = [
   #     "boto3>=1.42.22",
   #     "fastapi>=0.128.0",
   #     ...
   # ]
   # [tool.setuptools]
   # packages = { find = {} }
   # [tool.setuptools.dynamic]
   # dependencies = { file = "requirements.txt" }
   # Notes: This old configuration caused editable install confusion, self-dependency errors,
   # and dynamic dependencies conflicts. The current setup follows uv best practices.

5. Summary:
   - No need to run pip install -e . for development.
   - Use `uv run` to run Python scripts, tests, and other commands.
   - setup.py is retained only for historical reference and legacy compatibility.
"""