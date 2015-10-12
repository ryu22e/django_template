from invoke import run, task


@task
def pip_compile_all():
    """
    Call pip-compile for all 'in' files.
    """
    for f in ('local', 'production', 'test'):
        run('pip-compile requirements/{}.in'.format(f))
