import environ
import settings

def list_of_tuples(*args, **kwargs):
  default = kwargs.pop('default', [])
  l = env(*args, default=None)
  if not l:
    return default
  n = 2
  assert len(l) % n == 0
  res = []
  for i in range(0, len(l), n):
    res.append(l[i: i + n])
  return res

env = environ.Env()

SERVER_PREFIX = 'zeus'
DEBUG = env.bool('ZEUS_DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

ADMINS = list_of_tuples('ZEUS_ADMINS', default=settings.ADMINS)
ELECTION_ADMINS = ADMINS
MANAGERS = ADMINS

DATABASES = {
    'default': env.db('ZEUS_DATABASE_URL')
}

TIME_ZONE = env('ZEUS_TIMEZONE', default='Europe/Athens')

LANGUAGE_CODE = env('ZEUS_LANGUAGE_CODE', default='el-gr')
LANGUAGES = list_of_tuples('ZEUS_LANGUAGES', default=(('el', 'Greek'),))

SECRET_KEY = env('ZEUS_SECRET_KEY')

URL_HOST = env("ZEUS_URL_HOST", default="http://localhost")
SECURE_URL_HOST = env("ZEUS_SECURE_URL_HOST", default="https://localhost")

ALLOWED_HOSTS = env.list("ZEUS_HOSTS")

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/srv/zeus-data/emails'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': '/srv/zeus-data/zeus.log'
        }
    }
}

STATIC_ROOT = '/srv/zeus-data/'
STATIC_ROOT = '/srv/zeus-data/static/'
STATIC_URL = '/' + SERVER_PREFIX.strip('/') + '/static/'
MEDIA_ROOT = '/srv/zeus-data/media/'


STATICFILES_DIRS = (
    "/srv/zeus_app/server_ui/media/",
)

ZEUS_RESULTS_PATH     = '/srv/zeus-data/results/'
ZEUS_MIXES_PATH       = '/zrv/zeus-data/media/zeus_mixes/'
ZEUS_PROOFS_PATH      = '/srv/zeus-data/zeus_proofs/'
ZEUS_ELECTION_LOG_DIR = '/srv/zeus-data/election_logs/'

HELIOS_CRYPTOSYSTEM_PARAMS = {}
HELIOS_CRYPTOSYSTEM_PARAMS['p'] = 19936216778566278769000253703181821530777724513886984297472278095277636456087690955868900309738872419217596317525891498128424073395840060513894962337598264322558055230566786268714502738012916669517912719860309819086261817093999047426105645828097562635912023767088410684153615689914052935698627462693772783508681806906452733153116119222181911280990397752728529137894709311659730447623090500459340155653968608895572426146788021409657502780399150625362771073012861137005134355305397837208305921803153308069591184864176876279550962831273252563865904505239163777934648725590326075580394712644972925907314817076990800469107L
HELIOS_CRYPTOSYSTEM_PARAMS['q'] = 9968108389283139384500126851590910765388862256943492148736139047638818228043845477934450154869436209608798158762945749064212036697920030256947481168799132161279027615283393134357251369006458334758956359930154909543130908546999523713052822914048781317956011883544205342076807844957026467849313731346886391754340903453226366576558059611090955640495198876364264568947354655829865223811545250229670077826984304447786213073394010704828751390199575312681385536506430568502567177652698918604152960901576654034795592432088438139775481415636626281932952252619581888967324362795163037790197356322486462953657408538495400234553L
HELIOS_CRYPTOSYSTEM_PARAMS['g'] = 19167066187022047436478413372880824313438678797887170030948364708695623454002582820938932961803261022277829853214287063757589819807116677650566996585535208649540448432196806454948132946013329765141883558367653598679571199251774119976449205171262636938096065535299103638890429717713646407483320109071252653916730386204380996827449178389044942428078669947938163252615751345293014449317883432900504074626873215717661648356281447274508124643639202368368971023489627632546277201661921395442643626191532112873763159722062406562807440086883536046720111922074921528340803081581395273135050422967787911879683841394288935013751L
