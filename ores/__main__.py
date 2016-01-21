#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ores
import argparse


def _print_check_result(result):
    for res in result:
        print("* edit: {}".format(res['edit']))
        print("  ** prediction: {}".format(res['prediction']))
        print("  ** true probability: {}".format(res['true_prob']))
        print("  ** false probability: {}".format(res['false_prob']))
        print("")


def main():
    parser = argparse.ArgumentParser(
        prog='ores',
        description='Query the ORES API with Python.'
        )

    subparsers = parser.add_subparsers(title='Subcommands',
                                       dest='subparser_name',
                                       description='valid subcommands',
                                       help='Additional help')

    # Query
    parser_query = subparsers.add_parser('query')
    parser_query.add_argument(
        'query_string',
        type=str,
        help="A free-form query"
        )

    # List wikis
    parser_list_wikis = subparsers.add_parser('list-wikis')

    # List models
    parser_list_models = subparsers.add_parser('list-models')
    parser_list_models.add_argument(
        'project',
        type=str,
        help="A Wikimedia project, supported projects can be obtained with "
             "list_wikis."
        )

    # Check reverted
    parser_check_revert = subparsers.add_parser('check-reverted')

    parser_check_revert.add_argument(
        'project',
        type=str,
        help="A Wikimedia project, supported projects can be obtained with "
             "list_wikis."
        )
    parser_check_revert.add_argument(
        'edits',
        type=int,
        nargs='+',
        help="A list of edit IDs, as integers."
        )

    # Check goodfaith
    parser_check_good = subparsers.add_parser('check-goodfaith')

    parser_check_good.add_argument(
        'project',
        type=str,
        help="A Wikimedia project, supported projects can be obtained with "
             "list_wikis."
        )
    parser_check_good.add_argument(
        'edits',
        type=int,
        nargs='+',
        help="A list of edit IDs, as integers."
        )

    # Check damage
    parser_check_damage = subparsers.add_parser('check-damaging')

    parser_check_damage.add_argument(
        'project',
        type=str,
        help="A Wikimedia project, supported projects can be obtained with "
             "list_wikis."
        )
    parser_check_damage.add_argument(
        'edits',
        type=int,
        nargs='+',
        help="A list of edit IDs, as integers."
        )

    args = parser.parse_args()

    if args.subparser_name == 'query':
        result = ores.ores_query(args.query_string)
        print(result)

    elif args.subparser_name == 'list-wikis':
        result = ores.list_wikis()

        print("Available wikis")
        print("---------------")
        print("")
        for wiki in result:
            print("* {}".format(wiki))
        print("")

    elif args.subparser_name == 'list-models':
        result = ores.list_models(args.project)

        print("Available models for wiki: {}".format(args.project))
        print("---------------------------" + "-"*len(args.project))
        print("")
        for wiki in result:
            print("* {}".format(wiki))
        print("")

    elif args.subparser_name == 'check-reverted':
        result = ores.check_reverted(args.project, args.edits)
        print("Check reverted probability for wiki: {}".format(args.project))
        print("-------------------------------------" + "-"*len(args.project))
        _print_check_result(result)

    elif args.subparser_name == 'check-goodfaith':
        result = ores.check_reverted(args.project, args.edits)
        print("Check goodfaith probability for wiki: {}".format(args.project))
        print("--------------------------------------" + "-"*len(args.project))
        _print_check_result(result)

    elif args.subparser_name == 'check-damaging':
        result = ores.check_reverted(args.project, args.edits)
        print("Check damaging probability for wiki: {}".format(args.project))
        print("-------------------------------------" + "-"*len(args.project))
        _print_check_result(result)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
