from argparse import ArgumentParser
import getpass

from keeptrackd import (
        importer,
        tracker,
        config,
        dbmanager
        )


class KeepTrackd:
    def __init__(self):
        self.db = dbmanager.DBManager()

    def add_target(self, url):
        self.db.save(url, '')

    def remove_target(self, url):
        self.db.remove(url)

    def check(self, url):
        track = tracker.get_tracker(url)
        if track.check_update():
            track.postprocess()

    def check_all(self):
        for target in self.db.get_all():
            self.check(target[0])

    def list(self):
        return [target[0] for target in self.db.get_all()]


def __main__():

    trackd = KeepTrackd()

    parser = ArgumentParser(prog = 'PROG', description='keeptrackd command line interface')

    subparsers = parser.add_subparsers()


    def import_handler(args):
        url_list = importer.bookmark.get_chrome_bookmark_data(args.chrome_bookmark_path, args.chrome_bookmark_dir)
        for url in url_list:
            trackd.add_target(url)

    import_parser = subparsers.add_parser('import')
    import_parser.add_argument('--chrome-bookmark-path', type=str,
            default='/Users/{username}/Library/Application Support/Google/Chrome/Default/Bookmarks'.format(username = getpass.getuser()))
    import_parser.add_argument('--chrome-bookmark-dir', type=str, default='daily')
    import_parser.set_defaults(handler=import_handler)


    def check_handler(args):
        if args.only:
            trackd.check(args.only)
        else:
            trackd.check_all()

    check_parser = subparsers.add_parser('check')
    check_parser.add_argument('--only', type=str)
    check_parser.add_argument('--threads', type=int, default=4)
    check_parser.set_defaults(handler=check_handler)


    def add_handler(args):
        trackd.add_target(args.url)

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('url', type=str)
    add_parser.set_defaults(handler=add_handler)


    def remove_handler(args):
        trackd.remove_target(args.url)

    remove_parser = subparsers.add_parser('remove')
    remove_parser.add_argument('url', type=str)
    remove_parser.set_defaults(handler=remove_handler)

    
    def list_handler(args):
        for url in trackd.list():
            print(url)

    list_parser = subparsers.add_parser('list')
    list_parser.set_defaults(handler=list_handler)


    def config_handler(args):
        if args.database_filename:
            config.add('database_filename', args.database_filename)
        if args.chrome_binary_location:
            config.add('chrome_binary_location', args.chrome_binary_location)


    config_parser = subparsers.add_parser('config')
    config_parser.add_argument('--database-filename', type=str, default='keeptrackd.db')
    config_parser.add_argument('--chrome-binary-location', type=str, default='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    config_parser.set_defaults(handler=config_handler)


    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()