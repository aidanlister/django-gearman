import gearman
from django.conf import settings

class DjangoGearmanClient(gearman.GearmanClient):
    """ Gearman client which automatically connects to configured server. """
    def __init__(self, **kwargs):
        return super(DjangoGearmanClient, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)


class DjangoGearmanWorker(gearman.GearmanWorker):
    """ Gearman workder which automatically connects to the configured server. """

    def __init__(self, **kwargs):
        return super(DjangoGearmanWorker, self).__init__(
                settings.GEARMAN_SERVERS, **kwargs)

def check_request_status(job_request):
    """ Debugging function to check the status of a request. """
    if job_request.complete:
        print "Job %s finished!  Result: %s - %s" % (job_request.job.unique, job_request.state, job_request.result)
    elif job_request.timed_out:
        print "Job %s timed out!" % job_request.unique
    elif job_request.state == JOB_UNKNOWN:
        print "Job %s connection failed!" % job_request.unique
