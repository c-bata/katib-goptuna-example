import argparse
import logging

logging.basicConfig(filename='/var/log/katib.log', level=logging.DEBUG)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x1", dest='x1', type=float)
    parser.add_argument("--x2", dest='x2', type=float)

    args = parser.parse_args()
    print(args.x1, args.x2)

    evaluation = (args.x1 - 5) ** 2 + (args.x2 + 5) ** 2

    metric_msg = f'{{metricName: accuracy, metricValue: {evaluation:.4f}}};'
    print(metric_msg)

    logging.info(f'\n{metric_msg}\n')


if __name__ == '__main__':
    main()
