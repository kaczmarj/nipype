# Generated by Neurodocker v0.3.1-19-g8d02eb4.
#
# Thank you for using Neurodocker. If you discover any issues
# or ways to improve this software, please submit an issue or
# pull request on our GitHub repository:
#     https://github.com/kaczmarj/neurodocker
#
# Timestamp: 2017-11-03 23:59:36

FROM kaczmarj/nipype:base

ARG DEBIAN_FRONTEND=noninteractive

#----------------------------------------------------------
# Install common dependencies and create default entrypoint
#----------------------------------------------------------
ENV LANG="en_US.UTF-8" \
    LC_ALL="C.UTF-8" \
    ND_ENTRYPOINT="/neurodocker/startup.sh"
RUN apt-get update -qq && apt-get install -yq --no-install-recommends  \
    	apt-utils bzip2 ca-certificates curl locales unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && localedef --force --inputfile=en_US --charmap=UTF-8 C.UTF-8 \
    && chmod 777 /opt && chmod a+s /opt \
    && mkdir -p /neurodocker \
    && if [ ! -f "$ND_ENTRYPOINT" ]; then \
         echo '#!/usr/bin/env bash' >> $ND_ENTRYPOINT \
         && echo 'set +x' >> $ND_ENTRYPOINT \
         && echo 'if [ -z "$*" ]; then /usr/bin/env bash; else $*; fi' >> $ND_ENTRYPOINT; \
       fi \
    && chmod -R 777 /neurodocker && chmod a+s /neurodocker
ENTRYPOINT ["/neurodocker/startup.sh"]

LABEL maintainer="The nipype developers https://github.com/nipy/nipype"

ENV MKL_NUM_THREADS="1" \
    OMP_NUM_THREADS="1"

# Create new user: neuro
RUN useradd --no-user-group --create-home --shell /bin/bash neuro
USER neuro

#------------------
# Install Miniconda
#------------------
ENV CONDA_DIR=/opt/conda \
    PATH=/opt/conda/bin:$PATH
RUN echo "Downloading Miniconda installer ..." \
    && miniconda_installer=/tmp/miniconda.sh \
    && curl -sSL -o $miniconda_installer https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && /bin/bash $miniconda_installer -b -p $CONDA_DIR \
    && rm -f $miniconda_installer \
    && conda config --system --prepend channels conda-forge \
    && conda config --system --set auto_update_conda false \
    && conda config --system --set show_channel_urls true \
    && conda clean -tipsy && sync

#-------------------------
# Create conda environment
#-------------------------
RUN conda create -y -q --name neuro \
    && sync && conda clean -tipsy && sync \
    && sed -i '$isource activate neuro' $ND_ENTRYPOINT

COPY ["docker/files/run_builddocs.sh", "docker/files/run_examples.sh", "docker/files/run_pytests.sh", "nipype/external/fsl_imglob.py", "/usr/bin/"]

COPY [".", "/src/nipype"]

USER root

# User-defined instruction
RUN chmod 777 -R /src/nipype && chmod +x /usr/bin/run_builddocs.sh /usr/bin/run_examples.sh /usr/bin/run_pytests.sh /usr/bin/fsl_imglob.py

# User-defined instruction
RUN mkdir /work && chown -R neuro /work

USER neuro

ARG PYTHON_VERSION_MAJOR="3"
ARG PYTHON_VERSION_MINOR="6"
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

#-------------------------
# Update conda environment
#-------------------------
RUN conda install -y -q --name neuro python=${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR} \
                                     icu=58.1 \
                                     libxml2 \
                                     libxslt \
                                     matplotlib \
                                     mkl \
                                     numpy \
                                     pandas \
                                     psutil \
                                     scikit-learn \
                                     scipy \
                                     traits=4.6.0 \
    && sync && conda clean -tipsy && sync \
    && /bin/bash -c "source activate neuro \
      && pip install -q --no-cache-dir -e /src/nipype[all]" \
    && sync

LABEL org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.name="NIPYPE" \
      org.label-schema.description="NIPYPE - Neuroimaging in Python: Pipelines and Interfaces" \
      org.label-schema.url="http://nipype.readthedocs.io" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="https://github.com/nipy/nipype" \
      org.label-schema.version="$VERSION" \
      org.label-schema.schema-version="1.0"

#--------------------------------------
# Save container specifications to JSON
#--------------------------------------
RUN echo '{ \
    \n  "pkg_manager": "apt", \
    \n  "check_urls": false, \
    \n  "instructions": [ \
    \n    [ \
    \n      "base", \
    \n      "kaczmarj/nipype:base" \
    \n    ], \
    \n    [ \
    \n      "label", \
    \n      { \
    \n        "maintainer": "The nipype developers https://github.com/nipy/nipype" \
    \n      } \
    \n    ], \
    \n    [ \
    \n      "env", \
    \n      { \
    \n        "MKL_NUM_THREADS": "1", \
    \n        "OMP_NUM_THREADS": "1" \
    \n      } \
    \n    ], \
    \n    [ \
    \n      "user", \
    \n      "neuro" \
    \n    ], \
    \n    [ \
    \n      "miniconda", \
    \n      { \
    \n        "env_name": "neuro", \
    \n        "activate": "true" \
    \n      } \
    \n    ], \
    \n    [ \
    \n      "copy", \
    \n      [ \
    \n        "docker/files/run_builddocs.sh", \
    \n        "docker/files/run_examples.sh", \
    \n        "docker/files/run_pytests.sh", \
    \n        "nipype/external/fsl_imglob.py", \
    \n        "/usr/bin/" \
    \n      ] \
    \n    ], \
    \n    [ \
    \n      "copy", \
    \n      [ \
    \n        ".", \
    \n        "/src/nipype" \
    \n      ] \
    \n    ], \
    \n    [ \
    \n      "user", \
    \n      "root" \
    \n    ], \
    \n    [ \
    \n      "run", \
    \n      "chmod 777 -R /src/nipype && chmod +x /usr/bin/run_builddocs.sh /usr/bin/run_examples.sh /usr/bin/run_pytests.sh /usr/bin/fsl_imglob.py" \
    \n    ], \
    \n    [ \
    \n      "run", \
    \n      "mkdir /work && chown -R neuro /work" \
    \n    ], \
    \n    [ \
    \n      "user", \
    \n      "neuro" \
    \n    ], \
    \n    [ \
    \n      "arg", \
    \n      { \
    \n        "PYTHON_VERSION_MAJOR": "3", \
    \n        "PYTHON_VERSION_MINOR": "6", \
    \n        "BUILD_DATE": "", \
    \n        "VCS_REF": "", \
    \n        "VERSION": "" \
    \n      } \
    \n    ], \
    \n    [ \
    \n      "miniconda", \
    \n      { \
    \n        "env_name": "neuro", \
    \n        "conda_install": "python=${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR} icu=58.1 libxml2 libxslt matplotlib mkl numpy pandas psutil scikit-learn scipy traits=4.6.0", \
    \n        "pip_opts": "-e", \
    \n        "pip_install": "/src/nipype[all]" \
    \n      } \
    \n    ], \
    \n    [ \
    \n      "label", \
    \n      { \
    \n        "org.label-schema.build-date": "$BUILD_DATE", \
    \n        "org.label-schema.name": "NIPYPE", \
    \n        "org.label-schema.description": "NIPYPE - Neuroimaging in Python: Pipelines and Interfaces", \
    \n        "org.label-schema.url": "http://nipype.readthedocs.io", \
    \n        "org.label-schema.vcs-ref": "$VCS_REF", \
    \n        "org.label-schema.vcs-url": "https://github.com/nipy/nipype", \
    \n        "org.label-schema.version": "$VERSION", \
    \n        "org.label-schema.schema-version": "1.0" \
    \n      } \
    \n    ] \
    \n  ], \
    \n  "generation_timestamp": "2017-11-03 23:59:36", \
    \n  "neurodocker_version": "0.3.1-19-g8d02eb4" \
    \n}' > /neurodocker/neurodocker_specs.json
