.. _contribute:

************************
Contribute to WRIMS Docs
************************

.. _WRIMS Docs Repo: https://github.com/CentralValleyModeling/wrims-docs


First off: thank you for helping to contribute to WRIMS documentation. This is an 
open-source project led by the Department of Water Resources. If you are an external 
collaborator, please let us know if you have any questions about contributing by 
submitting an Issue on the `WRIMS Docs Repo`_.

Contribution Steps
------------------

.. _requirements.txt: https://github.com/CentralValleyModeling/wrims-docs/blob/main/docs/requirements.txt

1. Install Python and git
^^^^^^^^^^^^^^^^^^^^^^^^^

Instructions can be found elsewhere.

- Download `Python <https://www.python.org/downloads>`__
- Download `git scm <https://git-scm.com/install/>`__

2. Clone the project
^^^^^^^^^^^^^^^^^^^^

``git clone`` the project that you want to help with. See the :ref:`home<home>` 
page for a description of each of the projects if you aren't sure where to put 
your changes. 

3. Set up the environment
^^^^^^^^^^^^^^^^^^^^^^^^^

Set up the virtual environment used for building the documentation locally. 
The environment specification can be found in `requirements.txt`_. This environment 
should be identical for WRIMS Docs, WRIMS Engine, WRIMS GUI, and WRESL+.

===============    ===========================================================
Package            Details
===============    ===========================================================
``sphinx``         We use Sphinx to build the HTML docs from ``.rst.`` files. 
``intersphinx``    We use this in order to link between different subprojects.
===============    ===========================================================

4. Create a ``docs/``  branch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new branch so you can keep your changes separate from other activites 
on the repositories. 

.. note::
    Branches that make changes to documentation should always start with  ``docs/``.

5. Make your changes
^^^^^^^^^^^^^^^^^^^^

Do your thing. Refer to the following references for help with all of the tools
we use.

.. _Sphinx Basics: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

=======  =========
Tool     Reference
=======  =========
Sphinx   `Sphinx Basics`_
=======  =========

Most likely, you won't need to change the ``docs/conf.py``, 
``docs/requorements.txt``, nor the ``.readthedocs.yaml`` configuration files. 
Most content changes only require creating/editing ``*.rst`` files, and adding 
images or other static content. 

.. warning::
    If the static content that you are adding has a large memory footprint in 
    git, consider opening an issue on the repo to discuss using ``git lfs``. Do
    not make this decision on your own, as there is a limit to ``lfs`` usage on
    these repositories.

6. Check your changes
^^^^^^^^^^^^^^^^^^^^^

Build the documentation locally by:

``>>> python -m sphinx docs build -E``

This will use sphinx to read the ``.rst`` files in the ``docs`` directory, and 
output the rendered html files to the ``build`` directory. Open the html files 
in your browser of choice to make sure that things look like what you expect 
them to.

Also review the output from Sphinx, and make sure that your changes don't add 
any new warnings or errors to the output.

Make sure to check the following common issues:

- Table of Contents
- Links to external pages
- Links to other WRIMS Docs projects
- Image sizes

7. Push your changes, and open a Pull Request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After you've checked your changes, push them to the GitHub repo. Then go to the 
GitHub website and open a Pull Request into the ``main`` branch. A maintainer 
will be notifed that your request was made, and will be in contact. If they 
approve your changes, it is up to you to click the big green button!