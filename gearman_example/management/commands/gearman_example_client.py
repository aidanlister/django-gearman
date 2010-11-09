from django.core.management.base import NoArgsCommand
from django_gearman import DjangoGearmanClient


class Command(NoArgsCommand):
    help = "Execute an example command with the django_gearman interface"
    __doc__ = help

    def handle_noargs(self, **options):
        client = DjangoGearmanClient()

        print "Synchronous Gearman Call"
        print "------------------------"
        sentence = "The quick brown fox jumps over the lazy dog."
        print "Reversing example sentence: '%s'" % sentence
        # call "reverse" job defined in gearman_example app (i.e., this app)
        res = client.submit_job("gearman_example.reverse", sentence)
        print "Result: '%s'" % res.result
        print

        print "Asynchronous Gearman Call"
        print "-------------------------"
        print "Notice how this app exits, while the workers still work on the tasks."
        for i in range(4):
            client.submit_job(
                'gearman_example.background_counting', wait_until_complete=False
            )

