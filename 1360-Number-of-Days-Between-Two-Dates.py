class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        from datetime import datetime
        
        dt = datetime.strptime(date1, '%Y-%m-%d').date()
        dt2 = datetime.strptime(date2, '%Y-%m-%d').date()
        
        if (dt > dt2):
            res = (dt - dt2).days
        else:
            res = (dt2 - dt).days
        return res