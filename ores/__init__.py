#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

__version__ = '0.0.1'


def ores_query(path):
    ores_url = 'http://ores.wmflabs.org/{}'
    headers = {'User-Agent': 'ORES Python Client'}

    url = ores_url.format(path)
    response = requests.get(url, headers=headers)

    try:
        result = response.json()
    except ValueError:
        result = None

    return result


def list_wikis():
    """
    List supported projects.

    Usage
    -----

    list_wikis()


    Description
    -----------

    list_wikis() lists Wikimedia projects that support some or all of the ORES
    models.


    Return
    ------

    A list of projects supported by ORES, as strings
    """
    result = ores_query("scores/")

    return result.get('contexts') if result else None


def list_models(project):
    """
    List model information

    Usage
    -----

    list_models(project)


    Description
    -----------

    list_models lists information about the models for a particular wiki,
    including what models are available, how they have been trained,
    information about the model's accuracy and ROC, and the model's version.


    Attributes
    ----------
    project : string
        A Wikimedia project, supported projects can be obtained with
        list_wikis.

    Return
    ------


    Notes
    -----
    See also list_wikis() for retrieving the list of supported projects, and
    check_reverted and similar for actual checking against models.
    """

    result = ores_query('scores/{project}/'.format(project=project))

    return result.get('models') if result else None


def _parse_response(project, data):
    """
    Helper function
    """

    result = None
    if data:
        response = data.values()[0]

        if 'error' in response:
            result = {'edit': data.keys()[0],
                      'project': project,
                      'prediction': None,
                      'false_prob': None,
                      'true_prob': None
                      }
        else:
            result = {'edit': data.keys()[0],
                      'project': project,
                      'prediction': response['prediction'],
                      'false_prob': response['probability']['false'],
                      'true_prob': response['probability']['true']
                      }

    return result


def check_reverted(project, edits):
    """
    Check revert probabilities

    Usage
    -----

    check_reverted(project, edits)


    Description
    -----

    check_reverted identifies whether or not an edit is considered likely, by
    the ORES models, to be reverted.


    Attributes
    ----------

    project : string
        A Wikimedia project, supported projects can be obtained with
        list_wikis.

    edits: iterable
        An iterable of edit IDs, as integers.


    Return
    ------
    A dictionary with five fieds:

    1. edit, the edit ID;
    2. project, the project;
    3. prediction, whether the model predicts that the edit will be reverted;
    4. false_prob, the probability that the model's prediction is wrong;
    5. true_prob, the probability that the model's prediction is correct.

    In the event of an error (due to the edit not being available) None will be
    returned in that row.


    Notes
    -----
    See also check_goodfaith to identify if a set of edits were made in good
    faith, and check_damaging to check if a set of edits were
    damaging.

    Examples
    --------

    A simple, single-diff example

    revert_data = check_reverted("enwiki", [34854345])
    """

    if not hasattr(edits, '__iter__'):
        raise TypeError('edits must be an iterable')

    for edit in edits:
        data = ores_query("scores/{project}/reverted/{edit}"
                          .format(project=project, edit=edit))

        yield _parse_response(project, data)


def check_goodfaith(project, edits):
    """
    Check good-faith probability


    Usage
    -----

    check_goodfaith(project, edits)


    Description
    -----

    check_goodfaith identifies whether or not an edit was made in 'good faith'
    - whether it was well-intentioned, even if it is not a high-quality
    contribution.


    Attributes
    ----------

    project : string
        A Wikimedia project, supported projects can be obtained with
        list_wikis.

    edits: iterable
        An iterable of edit IDs, as integers.


    Return
    ------
    A dictionary with five fieds:

    1. edit, the edit ID;
    2. project, the project;
    3. prediction, whether the model predicts that the edit will be reverted;
    4. false_prob, the probability that the model's prediction is wrong;
    5. true_prob, the probability that the model's prediction is correct.

    In the event of an error (due to the edit not being available) None will be
    returned in that row.


    Notes
    -----
    See also check_reverted to identify if a set of edits are likely to be
    reverted, and \code{\link{check_damaging}} to check if a set of edits were
    damaging.

    Examples
    --------

    A simple, single-diff example

    goodfaith_data <- check_goodfaith("enwiki", 34854345)
    """

    if not hasattr(edits, '__iter__'):
        raise TypeError('edits must be an iterable')

    for edit in edits:
        data = ores_query("scores/{project}/goodfaith/{edit}"
                          .format(project=project, edit=edit))

        yield _parse_response(project, data)


def check_damaging(project, edits):
    """
    Check damaging probability


    Usage
    -----

    check_damaging(project, edits)

    Description
    -----

    check_damaging identifies whether or not an edit was damaging - the type
    that caused actual harm to an article.


    Attributes
    ----------

    project : string
        A Wikimedia project, supported projects can be obtained with
        list_wikis.

    edits: iterable
        An iterable of edit IDs, as integers.


    Return
    ------
    A dictionary with five fieds:

    1. edit, the edit ID;
    2. project, the project;
    3. prediction, whether the model predicts that the edit will be reverted;
    4. false_prob, the probability that the model's prediction is wrong;
    5. true_prob, the probability that the model's prediction is correct.

    In the event of an error (due to the edit not being available) None will be
    returned in that row.


    Notes
    -----
    See also check_goodfaith to identify if a set of edits were made in good
    faith, and check_reverted to check if a set of edits are likely to be
    reverted.

    Examples
    --------

    A simple, single-diff example

    damaging_data = check_damaging("enwiki", [34854345])
    """

    if not hasattr(edits, '__iter__'):
        raise TypeError('edits must be an iterable')

    for edit in edits:
        data = ores_query("scores/{project}/goodfaith/{edit}"
                          .format(project=project, edit=edit))

        yield _parse_response(project, data)
