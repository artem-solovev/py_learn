import sys

s = "The sword is truth"

print( '{0}'.format( s ) ) # 'The sword is truth'

print( '{0:25}'.format( s ) ) # 'The sword is truth '

print( '{0:>25}'.format( s ) ) # '    The sword is truth'

print( '{0:^25}'.format( s ) ) # '  The sword is truth  '

print( '{0:-^25}'.format( s ) ) # '---The sword is truth----'

print( '{0:.<25}'.format( s ) ) # 'The sword is truth.......'

print( '{0:.10}'.format( s ) ) # 'The sword '

print( '{0:b} {0:o} {0:x} {0:X}'.format( 14613198 ) )
