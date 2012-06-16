import pycassa
from pycassa.system_manager import *

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        sys = SystemManager()

        # If there is already a Twissandra keyspace, we have to ask the user
        # what they want to do with it.
        if 'Activibe' in sys.list_keyspaces():
            msg = 'Looks like you already have a Activibe keyspace.\nDo you '
            msg += 'want to delete it and recreate it? All current data will '
            msg += 'be deleted 123! (y/n): '
            resp = raw_input(msg)
            if not resp or resp[0] != 'y':
                print "Ok, then we're done here."
                return
            sys.drop_keyspace('Activibe')

        sys.create_keyspace('Activibe', SIMPLE_STRATEGY, {'replication_factor': '1'})#change rep factor to 3 later on when deployed on cluster, 3 is standard
        sys.create_column_family('Activibe', 'UserInfo', comparator_type=UTF8_TYPE)
        sys.create_column_family('Activibe', 'DoctorInfo', comparator_type=UTF8_TYPE)
        sys.create_column_family('Activibe', 'DoctorFollowingUser', comparator_type=UTF8_TYPE)
        sys.create_column_family('Activibe', 'UserStatus', comparator_type=UTF8_TYPE)
        sys.create_column_family('Activibe', 'UserServedByDoctors', comparator_type=UTF8_TYPE)
        

        print 'Activibe creation done!'

        if 'Twissandra' in sys.list_keyspaces():
            msg = 'Looks like you already have a Twissandra keyspace.\nDo you '
            msg += 'want to delete it and recreate it? All current data will '
            msg += 'be deleted123! (y/n): '
            resp = raw_input(msg)
            if not resp or resp[0] != 'y':
                print "Ok, then we're done here."
                return
            sys.drop_keyspace('Twissandra')

        sys.create_keyspace('Twissandra', SIMPLE_STRATEGY, {'replication_factor': '1'})
        sys.create_column_family('Twissandra', 'User', comparator_type=UTF8_TYPE)
        sys.create_column_family('Twissandra', 'Friends', comparator_type=BYTES_TYPE)
        sys.create_column_family('Twissandra', 'Followers', comparator_type=BYTES_TYPE)
        sys.create_column_family('Twissandra', 'Tweet', comparator_type=UTF8_TYPE)
        sys.create_column_family('Twissandra', 'Timeline', comparator_type=LONG_TYPE)
        sys.create_column_family('Twissandra', 'Userline', comparator_type=LONG_TYPE)

        print 'All done!'
