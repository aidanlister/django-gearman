from django.conf import settings
from gearman import GearmanClient, GearmanWorker


class DjangoGearmanClient(GearmanClient):
    """gearman client, automatically connecting to server"""

    def __call__(self, func, arg, uniq=None, **kwargs):
        raise NotImplementedError('Use do_task() or dispatch_background'\
                                  '_task() instead')

    def __init__(self, **kwargs):
        """instantiate Gearman client with servers from settings file"""
        return super(DjangoGearmanClient, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)


class DjangoGearmanWorker(GearmanWorker):
    """
    gearman worker, automatically connecting to server and discovering
    available jobs
    """

    def __init__(self, **kwargs):
        """instantiate Gearman worker with servers from settings file"""
        return super(DjangoGearmanWorker, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)
