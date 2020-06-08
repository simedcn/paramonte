#!/usr/bin/python
# Author:  Amir Shahmoradi
# Contact: shahmoradi@utexas.edu
####################################################################################################################################
####################################################################################################################################
####
####   ParaMonte: plain powerful parallel Monte Carlo library.
####
####   Copyright (C) 2012-present, The Computational Data Science Lab
####
####   This file is part of the ParaMonte library.
####
####   ParaMonte is free software: you can redistribute it and/or modify it
####   under the terms of the GNU Lesser General Public License as published
####   by the Free Software Foundation, version 3 of the License.
####
####   ParaMonte is distributed in the hope that it will be useful,
####   but WITHOUT ANY WARRANTY; without even the implied warranty of
####   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
####   GNU Lesser General Public License for more details.
####
####   You should have received a copy of the GNU Lesser General Public License
####   along with the ParaMonte library. If not, see,
####
####       https://github.com/cdslaborg/paramonte/blob/master/LICENSE
####
####   ACKNOWLEDGMENT
####
####   As per the ParaMonte library license agreement terms,
####   if you use any parts of this library for any purposes,
####   we ask you to acknowledge the use of the ParaMonte library
####   in your work (education/research/industry/development/...)
####   by citing the ParaMonte library as described on this page:
####
####       https://github.com/cdslaborg/paramonte/blob/master/ACKNOWLEDGMENT.md
####
####################################################################################################################################
####################################################################################################################################
"""
This is the Python interface to ParaMonte: Plain Powerful Parallel Monte Carlo library.

What is ParaMonte?
==================

ParaMonte is a serial / parallel library of Monte Carlo routines for sampling mathematical
objective functions of arbitrary-dimensions, in particular, the posterior distributions
of Bayesian models in data science, Machine Learning, and scientific inference, with the
design goal of unifying the

    **automation** of Monte Carlo simulations,  

    **user-friendliness** of the library,  

    **accessibility** from multiple programming environments,  

    **high-performance** at runtime, and,  

    **scalability** across many parallel processors.  

For more information on the installation, usage, and examples, visit:

    https://www.cdslab.org/paramonte

For the API documentation, visit:

    https://www.cdslab.org/paramonte/notes/api/python

ParaMonte samplers
================== 

The routines currently supported by the ParaMonte Python library include:

    **ParaDRAM**

        Parallel Delayed-Rejection Adaptive Metropolis-Hastings Markov Chain Monte Carlo Sampler.
        For a quick start, example scripts, and instructions on how to use he ParaDRAM sampler,
        type the following commands in your Python session,

        .. code-block:: python
            :linenos:

            ##################################
            import paramonte as pm
            pm.helpme("paradram") # the input value is case-insensitive
            ##################################

        or,

        .. code-block:: python
            :linenos:

            ##################################
            import paramonte as pm
            help(pm.ParaDRAM) # get help on ParaDRAM sampler class
            ##################################

Naming conventions
==================

+   The camelCase naming style is used throughout the entire ParaMonte library, across
    all programming languages. The ParaMonte library is a multi-language cross-platform
    library. To increase the consistently and similarities of all implementations,
    a single naming convension had to be used for all different languages.

+   All simulation specifications start with a lowercase letter, including
    scalar/vector/matrix int, float, string, or boolean variables.

+   The name of any variable that represents a vector of values is normally suffixed with ``Vec``,
    for example: ``startPointVec``, ``domainLowerLimitVec``, ...

+   The name of any variable that represents a matrix of values is normally suffixed with ``Mat``,
    for example: ``proposalStartCorMat``, ...

+   The name of any variable that represents a list of varying-size values is normally suffixed
    with ``List``, for example: ``variableNameList``, ...

+   All static functions or methods of classes begin with a lowercase verb.

+   Significant attempt has been made to end all boolean variables with a passive verb, such
    that the full variable name virtually forms  a proposition, that is, an English-language
    statement that should be either ``True`` or ``False``, set by the user.

Tips
====

+   When running the ParaMonte samplers, in particular on multiple cores in parallel,
    it would be best to close any such aggressive software/applications as
    **Dropbox**, **ZoneAlarm**, ... that can **interfere with the ParaMonte
    simulation output files**, potentially **causing the sampler to
    crash** before successful completion of the simulation.
    These situations should however happen only scarcely.

+   On Windows systems, when restarting an old interrupted ParaMonte simulation,
    ensure your Python session is also restarted before the simulation restart.
    This may be needed as Windows sometimes locks access to some or all of the
    simulation output files.

+   To unset an already-set input simulation specification, simply set the
    simulation attribute to None or re-instantiate the object.

-------------------------------------------------------------------------------
"""

import os as _os
import sys as _sys
import typing as _tp
_sys.path.append(_os.path.dirname(__file__))

import _paramonte as _pm

# objects exposed to the user

from _pmreqs import verify, build
from paradram import ParaDRAM
from _paramonte import version


__authors__ = "The Computational Data Science Lab @ The University of Texas"
__credits__ = "Peter O'Donnell Fellowship"
__version__ = version.interface.get()

verify(reset=False)

####################################################################################################################################

# def getVersion():
#     import warnings
#     msg = "getVersion() version will be removed in next release. Use paramonte.version object instead."
#     warnings.warn( msg, DeprecationWarning, stacklevel=2)
#     return __version__

####################################################################################################################################

def helpme( topic : _tp.Optional[str] = None ):
    """

    .. py:function:: helpme(topic = None)

    Prints help on the input object.

        **Parameters**

            topic
                A string value that is the name of an object in ``paramonte``
                module for which help is needed. To see the list of possible
                objects. try: ``pm.helpme("helpme")``

        **Returns**

            None

    """

    topics =    { "paradram": ParaDRAM
                , "version" : version
                , "verify"  : verify
                , "helpme"  : helpme
                , "build"   : build
                }

    usage   = "    Usage:\n\n" \
            + "        import paramonte as pm\n" \
            + "        pm.helpme()      # to get help on paramonte module.\n" \
            + "        pm.helpme(topic) # to get help on topic.\n\n" \
            + "    where `topic` in the above can be one of the following string values:\n\n" \
            + "        " + str(list(topics.keys()))
    
    if topic is None:
        print(__doc__)
    elif isinstance(topic,str) and (topic.lower() in topics.keys()):
        print(topics[topic.lower()].__doc__ + "\n")
        if topic.lower()=="helpme": _pm.note( msg = usage, methodName = "helpme()", marginTop = 0, marginBot = 1)
    else:
        try:
            topic = "(" + str(topic) + ") "
        except:
            topic = ""
        _pm.warn( msg   = "The requested object " + topic + "does not exist in paramonte module.\n\n"
                        + usage
                , methodName = "helpme()"
                , marginTop = 1
                , marginBot = 1
                )

    return None
