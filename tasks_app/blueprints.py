"""All Flask blueprints for the entire application
They shall be imported by application.py. Blueprint URL paths are defined here as well
"""

from flask import Blueprint


def _factory(partial_module_string, url_prefix):
    """Generates blueprint objects for view modules.
    Positional arguments:
    partial_module_string -- string representing a view module without the absolute path (e.g. 'tasks.manager' for
        tasks_app.api.tasks.manager).
    url_prefix -- URL prefix passed to the blueprint.
    Returns:
    Blueprint instance for a module.
    """
    name = partial_module_string
    import_name = 'tasks_app.api.{}'.format(partial_module_string)
    return Blueprint(name, import_name, url_prefix=url_prefix)


tasks_manager = _factory('tasks.manager', '/api/v1/tasks')
tasks_exception = _factory('tasks.exception', '/api/v1/exception')

all_blueprints = (tasks_manager, tasks_exception)
