import math


def calculateStats(numbers):
    computed_stats = {'max': math.nan,
                      'min': math.nan,
                      'avg': math.nan}
    if numbers:
        computed_stats['max'] = max(numbers)
        computed_stats['min'] = min(numbers)
        computed_stats['avg'] = sum(numbers)/len(numbers)
    return computed_stats


class StatsAlerter:
    def __init__(self, maxThreshold, alerts: list):
        self.max_threshold = maxThreshold
        self.alerts = alerts

    def checkAndAlert(self, numbers):
        stats = calculateStats(numbers)
        if stats['max'] > self.max_threshold:
            for alert in self.alerts:
                if hasattr(alert, 'emailSent'):
                    alert.emailSent = True
                elif hasattr(alert, 'ledGlows'):
                    alert.ledGlows = True
                else:
                    pass


class EmailAlert:
    def __init__(self):
        self.emailSent = False


class LEDAlert:
    def __init__(self):
        self.ledGlows = False

