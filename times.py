import datetime


def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(intervals_a, intervals_b):
    """Compute all strictly overlapping time intervals between two lists of time ranges."""

    def parse_datetime(dt_str):
        return datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

    overlaps = []

    for start_a_str, end_a_str in intervals_a:
        start_a = parse_datetime(start_a_str)
        end_a = parse_datetime(end_a_str)

        for start_b_str, end_b_str in intervals_b:
            start_b = parse_datetime(start_b_str)
            end_b = parse_datetime(end_b_str)

            overlap_start = max(start_a, start_b)
            overlap_end = min(end_a, end_b)

            if overlap_start < overlap_end:
                overlaps.append((
                    overlap_start.strftime("%Y-%m-%d %H:%M:%S"),
                    overlap_end.strftime("%Y-%m-%d %H:%M:%S"),
                ))

    return overlaps

if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(compute_overlap_time(large, short))