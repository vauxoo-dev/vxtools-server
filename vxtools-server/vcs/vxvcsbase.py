#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Base class for VCS management
'''


class VxVcsBase(object):
    '''
    Abstract base class for VCS management
    '''

    def branch(self):
        '''
        Retuns the branch
        '''
        raise NotImplementedError

    def is_local(self):
        '''
        Is the branch local?

        :returns: True ir branch is local, false otherwise
        '''
        raise NotImplementedError

    def pull(self):
        '''
        Pull from remote repo
            {
                'old_rev_id': 'Rev id previous to the pull',
                'rev_id': 'Actual rev id',
                'remote': 'repo url',
                'master': r.get('master'),
                'status': r.get('status'),
                'stat': 'Status updated|DivergedBranches|'
            }

        :returns: Dictionary with the branch info
        '''
        raise NotImplementedError

    def get_remote_branch(self):
        '''
        Retuns remore url

        :returns: A string containing the repo url
        '''
        raise NotImplementedError

    def get_branch_info(self, password=False):
        '''
        Retuns remore url

        :returns: A string containing the repo url
        '''
        raise NotImplementedError
