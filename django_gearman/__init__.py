def check_request_status(job_request):
    """ Debugging function to check the status of a request. """
    if job_request.complete:
        print "Job %s finished!  Result: %s - %s" % (job_request.job.unique, job_request.state, job_request.result)
    elif job_request.timed_out:
        print "Job %s timed out!" % job_request.unique
    elif job_request.state == JOB_UNKNOWN:
        print "Job %s connection failed!" % job_request.unique
