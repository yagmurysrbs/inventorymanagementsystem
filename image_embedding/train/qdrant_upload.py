# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct
# import os
# import uuid
# from embedding_model import get_embedding

# # 1. Qdrant’a bağlan
# client = QdrantClient(host="localhost", port=6333)

# # 2. Koleksiyon oluşturs
# collection_name = "milk_embed_clip"
# vector_size = 2048  # ResNet50 embedding boyutu

# if client.collection_exists(collection_name=collection_name):
#     client.delete_collection(collection_name=collection_name)

# client.create_collection(
#     collection_name=collection_name,
#     vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
# )

# # 3. Alt klasörlerdeki tüm .jpg dosyaları için işlemi yap
# image_folder = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/milks"

# for root, _, files in os.walk(image_folder):
#     for file in files:
#         if file.endswith(".jpg"):
#             full_path = os.path.join(root, file)
#             try:
#                 vector = get_embedding(full_path)
#                 metadata = {
#                     "filename": file,
#                     "folder": os.path.basename(root)  # Hangi ürün klasöründen geldiğini belirt
#                 }
#                 point = PointStruct(
#                     id=str(uuid.uuid4()),
#                     vector=vector,
#                     payload=metadata
#                 )
#                 client.upsert(collection_name=collection_name, points=[point])
#                 print(f"{full_path} yüklendi.")
#             except Exception as e:
#                 print(f"Hata oluştu: {file} - {e}")

# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct
# import os
# import uuid
# from embedding_model import get_embedding  # Görselden embedding çıkaran fonksiyon

# # 1. Qdrant’a bağlan
# client = QdrantClient(host="localhost", port=6333)

# # 2. Koleksiyon oluştur
# collection_name = "sutasSutCollection"
# vector_size = 512  # CLIP embedding boyutu

# # Koleksiyon var mı kontrol et, yoksa oluştur
# if not client.collection_exists(collection_name=collection_name):
#     client.create_collection(
#         collection_name=collection_name,
#         vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
#     )


# # 3. Alt klasörlerdeki tüm .jpeg dosyaları için işlemi yap
# image_folder = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Gıda/Sütaş/Süt/YağlıSüt"

# for root, _, files in os.walk(image_folder):
#     for file in files:
#         if file.endswith(".jpg"):
#             full_path = os.path.join(root, file)
#             try:
#                 # Görselden embedding çıkar
#                 vector = get_embedding(full_path)
                
#                 # Ürün bilgisi ve kategorik yapı
#                 metadata = {
#                         "product_name": "Yağlı-Süt",
#                         "categories": ["Gıda", "Sütaş", "Sut", "YağlıSüt"]
#                 }

#                 # Qdrant’a ekle
#                 point = PointStruct(
#                     id=str(uuid.uuid4()),  # Her ürün için benzersiz ID oluştur
#                     vector=vector,  # Görselin embedding’i
#                     payload=metadata  # Kategorik ve diğer bilgileri içerir
#                 )
                
#                 # Veriyi Qdrant’a yükle
#                 client.upsert(collection_name=collection_name, points=[point])
#                 print(f"{full_path} yüklendi.")
#             except Exception as e:
#                 print(f"Hata oluştu: {file} - {e}")


"""
    # folder collection vektor
"""

# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct
# import os
# import uuid
# from embedding_model import calculate_mean_vector  # Görselden embedding çıkaran fonksiyon
# import numpy as np

# # Görsel dosya yolu (örnek olarak)

# vec1 = np.array([-0.009223196,-0.068934806,-0.094518825,0.110369176,-0.0021009895,-0.022287622,0.008604371,0.06253974,-0.019412413,0.017588962,-0.01625653,-0.054415666,0.04863591,0.009801627,-0.033860322,0.015342218,-0.07630223,-0.013126174,0.04501164,0.056153215,-0.024696322,0.016402822,-0.039916355,-0.010881013,-0.015750322,-0.09023714,0.026031762,0.028622536,-0.03553775,-0.063158706,-0.0443967,0.022488536,-0.009198532,0.028618217,0.020148369,0.07339706,-0.06631195,0.030602943,0.020862816,0.031462234,0.029017586,0.033842113,-0.0667448,0.055601247,0.07158064,-0.021968877,-0.056893684,-0.025484286,-0.05301241,-0.005674887,0.0072570248,-0.060811527,-0.013911435,-0.009370256,-0.11345098,-0.0017498458,-0.012276593,-0.022581384,0.038312364,-0.008779073,0.008317978,-0.076643996,0.050624654,0.014681708,-0.04491843,0.021069782,0.018454561,0.038268734,0.006745459,0.03165637,-0.05987055,-0.020439396,-0.04985991,0.028717473,0.034765262,-0.013880248,-0.13329773,0.0066818832,0.040942233,-0.027417673,-0.021584032,-0.012377469,-0.008343003,0.004244171,0.032352217,-0.034522146,0.052991793,-0.029108403,0.01880101,-0.013575627,0.040808834,0.011555808,0.006083502,0.034025468,-0.024113521,-0.0146383345,-0.03432306,0.025414957,-0.03672718,0.06776502,0.01491682,0.028629959,-0.015597088,-0.010403368,0.033470888,0.0067260247,-0.0059601245,0.14769617,0.018592125,0.000044938803,-0.03612926,0.02860819,0.04820869,0.04808421,0.004098194,-0.040320743,0.0027340506,0.0739485,-0.10159926,0.004759795,-0.046563413,0.019244466,-0.05120518,0.036939792,-0.03301737,-0.07511289,0.036952578,-0.041105304,-0.017326329,0.018110929,0.00746536,0.019919017,0.018971061,-0.036445856,0.0115491785,-0.0031252138,-0.021063633,0.027444711,0.0054858737,0.01199825,-0.025128921,0.05036483,0.059621762,-0.047422536,-0.021942379,-0.018804234,-0.03809189,0.026126396,-0.04053446,-0.012534926,-0.005537106,0.0828221,0.23111925,0.05086805,-0.0243008,0.037301216,-0.005819192,0.013840779,-0.010329973,-0.04889566,0.0046285777,0.053552795,-0.02320944,0.04502509,0.0394817,0.041709557,-0.060085155,-0.008629971,0.051688652,0.02227602,-0.009607271,-0.005602646,0.04157226,0.0014934151,-0.019737858,0.1522793,-0.004905256,0.019075692,-0.10688319,0.035982274,-0.023672797,-0.03217451,0.021771196,0.07019461,-0.002949622,0.042707004,-0.06445072,-0.0005509044,0.06184086,-0.04797115,-0.021391384,0.05724243,0.036584552,-0.024859704,0.016489822,0.010836074,-0.032364327,-0.035691503,-0.0043848287,-0.03699268,-0.04685016,-0.046447992,0.015831342,0.05663122,0.0145225525,0.021189103,0.09372505,-0.022725346,-0.008185782,-0.043805726,0.0278738,0.08222756,0.04076795,-0.04096752,-0.0009889036,-0.020880634,0.05290104,0.0045055333,0.036151376,-0.005879887,0.06200393,0.0035470312,-0.003350373,-0.024273336,0.016795026,-0.043997124,0.008143454,0.024140375,-0.027773235,0.0054086414,-0.01156354,0.0054840306,-0.015011848,0.0070435978,0.01399886,0.018185431,-0.03516636,0.03334777,0.047172222,0.045715544,-0.03780659,0.0907184,0.02482436,-0.005654588,-0.030659035,-0.07209685,0.00081322435,0.01072323,0.04328677,-0.020994063,0.0061005447,0.039633587,-0.027971767,-0.05988686,-0.0508001,0.04251169,0.008371433,-0.07762101,-0.003616733,-0.029705979,0.03377367,0.0028514906,0.04260685,0.016560694,0.0024466026,-0.07219589,-0.013232972,-0.03201866,0.057761382,-0.029920053,-0.03718173,-0.02917906,0.048865788,-0.044115733,-0.020383187,0.024507256,0.061372373,0.018090826,0.017369488,-0.067239195,0.014700847,-0.052473273,0.0036203098,0.04100466,-0.0053889677,-0.021218006,-0.022480765,0.031931218,-0.025849355,0.005460021,0.037476007,0.0169169,0.014593692,0.022647506,0.012999695,0.000083377716,-0.09382886,-0.035369378,-0.005080633,0.056283772,-0.0106744375,0.03687808,-0.03353578,-0.046386536,-0.105578065,-0.05856466,-0.0036284383,-0.23044291,-0.013414303,-0.042850725,0.024299737,0.002380944,0.028134812,0.018062055,0.067820944,0.029873554,-0.04471476,-0.034396194,0.0057977177,-0.052057687,-0.03748754,0.011390444,-0.004946208,0.08044214,-0.10063387,-0.038418636,0.044841953,0.021207882,-0.016763045,-0.019854877,-0.021010552,-0.0044111125,0.011755535,0.05604407,-0.00033119187,-0.01358061,-0.044682108,-0.004198535,0.025050499,0.026951054,0.021002423,-0.014136263,0.010649878,0.031908657,0.022580856,0.02544099,0.0054112594,-0.0060142158,-0.21013759,-0.08108821,-0.018736064,-0.05139654,-0.04234877,0.05069293,-0.077499524,-0.04297877,0.041784495,-0.031965677,-0.023131443,0.0073908684,0.046558168,0.016001198,-0.020306,0.010112714,-0.02966604,-0.022819087,0.008832508,0.024692763,-0.025928628,-0.027131956,-0.026779952,0.012391189,-0.006829642,-0.03547587,0.0035485597,-0.018480971,0.012747812,0.0024045906,-0.017119542,-0.01937688,0.019080954,0.058769662,-0.011317111,0.036827177,0.038463622,0.03807695,-0.0033898186,-0.057480603,-0.018268874,0.015567426,0.055550624,-0.0065957117,-0.018879274,-0.012974304,0.006857368,-0.044685513,-0.046444688,-0.0258529,0.026976991,0.04989676,0.02497797,0.07754042,0.018314943,0.009733882,-0.028115096,0.015062406,0.004152595,-0.050000865,0.024551058,-0.039975815,0.02585247,0.03280171,0.045442015,-0.021154026,0.0350242,0.038449533,0.010134582,0.05078208,0.027753707,-0.00022621134,-0.04325728,-0.043766066,-0.053379435,0.036036175,0.07223705,-0.022676386,-0.031446435,-0.048000164,-0.0012473369,-0.04862282,-0.05099743,0.099437095,0.0017976332,0.020752886,-0.042020246,0.04038142,-0.02516782,0.04194903,0.036776118,-0.024438243,0.046822548,-0.030058788,-0.03653941,-0.007905205,-0.09938189,0.037146427,0.0072993943,-0.003209689,0.0871467,-0.0066661756,0.033012684,0.037742537,-0.013336709,-0.029455403,-0.022193588,-0.15042146,0.011451059,-0.039485283,0.054611333,-0.03470324,0.01739206,-0.065499604,0.010282043,-0.04310015,0.006418391,0.029930804,0.032293957,0.03950193,0.020741828,-0.00033862115,-0.06572029,0.06394904,0.020130236,0.0076234536,-0.015469838,0.09171572,0.005444685,0.059983615,-0.018036777,-0.03281369,0.03977585,-0.071025684,-0.0606498,0.07198526,0.076421104,-0.037165202,0.06381166,0.011003474,0.0142985005,-0.07650824,0.048584186,0.01869016,0.051816598,-0.0038970064,0.052266,0.08028431,-0.059878185,-0.0213472,-0.017537514,-0.047569744,0.010344866,0.0014023309,-0.028839873,0.033310384,-0.028515354,0.002305571,0.03751491,0.024883041,-0.053834025,-0.010722564,0.0050660996,-0.03927542])
# vec2 = np.array([-0.013154524,-0.06297276,-0.05339157,0.039360475,-0.011889865,0.0067897122,0.0586064,0.041626416,-0.025744207,0.057482876,0.010792091,-0.0134853255,0.010600914,-0.023391064,-0.014876725,0.052197076,-0.09165709,-0.019429851,-0.0026979856,0.014777671,-0.053932354,0.02906198,-0.018808624,-0.018147642,-0.0078152,-0.11032297,0.0048372163,0.027322454,-0.011590769,-0.031929027,0.029950518,-0.015141387,-0.02481649,-0.014882437,0.052708045,0.02526949,-0.005527072,-0.0207111,0.03175519,0.010908678,0.02531527,0.006850269,-0.021374244,0.018464386,0.058664072,-0.046831388,-0.07313492,0.023840643,-0.043069735,-0.04854754,0.000018945433,-0.06631998,0.0101101715,0.011020769,-0.13436979,0.0035032674,-0.027353449,0.04038455,0.02586307,-0.009229294,0.04604396,-0.07737198,0.007879884,0.039757244,0.011546763,0.02756971,0.0039881854,0.065133534,-0.007514348,0.025534738,-0.06898595,-0.010654486,-0.068715625,0.022825822,0.001109206,-0.06650404,-0.10228431,-0.0006590473,0.03040786,-0.014531031,-0.006791933,0.03709732,-0.04002466,0.021546874,-0.004797794,-0.021282105,-0.018176127,0.004384175,-0.029375924,-0.084975645,0.011114382,-0.040118534,-0.0074556484,-0.0038363694,-0.019753955,-0.0029534244,-0.020507663,0.01778586,-0.0056103473,0.020362144,-0.031404942,0.034342706,0.017274497,-0.04064067,0.03955352,0.06602575,-0.06564975,0.13784339,0.025875075,-0.0322453,0.006600959,0.008517403,0.0004598607,0.016091287,-0.009150498,-0.05290427,-0.04015918,0.083241396,-0.0195276,-0.014612549,0.008866499,0.053848162,-0.04182027,0.048666183,0.011041135,-0.009061097,-0.024537867,0.015516496,-0.051258594,-0.006706954,-0.04400819,0.048885826,-0.033107378,-0.012742168,0.013685129,0.0103350645,-0.01720921,0.052732565,0.03209319,0.004902982,0.027136927,-0.0015657427,0.09966169,0.01887775,-0.05580257,-0.048587307,-0.042568125,0.0049488875,-0.012291971,0.020322321,0.0066379933,0.037452042,0.20668577,0.023701847,-0.015998686,0.06289546,0.0104778055,0.018808719,0.028306391,-0.026002906,0.04515087,0.07418737,-0.0043464517,0.04079737,0.024518056,0.10097877,-0.027296446,0.0011560564,-0.027549103,0.0037246156,-0.07553893,-0.014251496,0.04100548,-0.029944897,0.025668563,0.060418893,-0.0127996085,0.0001209888,-0.13083698,-0.030714205,-0.029504366,0.004204207,0.057675906,0.11059282,-0.01698756,0.009254728,-0.011356098,-0.038204648,0.014933936,-0.016909305,-0.0026359446,0.060766008,-0.009317094,-0.01778831,0.032527283,-0.011787879,-0.083602525,-0.013987638,-0.013461106,0.015778676,-0.038314003,-0.12476127,0.10193003,0.004079091,0.0016063548,0.020685274,0.008339355,0.011067327,0.030726355,0.034397155,0.055893146,0.088798426,0.029753212,0.05143416,0.02550926,0.009793756,0.0016015075,-0.03855543,0.014947718,0.020166494,0.028901463,-0.023837335,-0.013208175,-0.0012216697,0.0009598265,0.00040621546,0.0036013126,0.05455576,-0.052919514,0.0038933305,0.054235276,0.023507502,-0.12147066,0.009280111,0.0053165997,0.002470929,0.00090150605,0.01781044,0.0342275,0.014367781,-0.029702172,0.0703421,-0.020590845,0.028399542,-0.005893489,-0.071327284,-0.019902926,-0.0017405561,0.012458834,0.034077108,-0.0000070570036,0.049389556,-0.08075901,-0.06895783,-0.07120724,0.031013003,-0.015978739,-0.07684664,0.037212968,-0.059841953,-0.0031110395,0.008870556,0.01994473,0.032610744,-0.03668498,-0.036897693,0.029062849,0.0008709573,0.011109445,-0.02861039,-0.034383707,-0.008761046,0.045578916,-0.049063846,0.00065336004,0.044224188,0.022952925,0.04588953,0.0035707294,-0.09491658,0.038976353,-0.029777944,0.01815083,0.0069241202,-0.04671813,-0.02788658,-0.0045778346,0.0117715355,0.013974987,0.01729456,-0.053660024,0.040091615,-0.017124705,-0.03532661,-0.019880341,0.013259276,-0.07865292,-0.06916095,0.00681198,0.012283538,0.024514686,0.042486075,-0.008273343,-0.0823387,-0.09878539,0.037444666,0.039647885,-0.20575792,0.0067099542,-0.07915288,0.062090285,0.03266519,0.011576915,-0.018540349,0.021136196,0.10811283,-0.043594163,-0.06813047,-0.0297893,-0.012490248,-0.0032976212,-0.006498298,0.05725992,-0.0003931059,-0.12082762,-0.05961713,0.042260773,0.061426695,0.0158775,-0.03290608,0.0023615852,0.011404763,-0.0145725915,0.032587375,-0.000082381724,0.032656148,-0.021256935,-0.021312028,-0.018203357,0.007413365,0.029034758,0.055991735,0.02067854,0.058425933,0.046415932,0.023557255,0.023764879,-0.027359024,-0.11176348,-0.15255995,0.021715138,-0.01458897,-0.03988596,-0.0009604885,-0.035110068,-0.043694016,0.022682307,0.027780643,-0.0120691,0.0011950568,-0.002900261,-0.018548563,-0.031292032,0.015593426,-0.020382266,0.010969322,-0.0027691906,0.0012197013,-0.08390446,-0.012976387,-0.030722803,-0.015543965,0.020367185,-0.0872153,0.030894604,0.004916347,-0.021618633,0.00749764,-0.034198277,-0.023348188,0.021561434,0.0011957822,0.044008013,-0.008895216,-0.021918174,0.036598206,0.030821027,-0.018172044,-0.015042633,0.05736845,0.020657292,0.027841205,0.003692817,-0.025381476,0.027842896,-0.027148673,-0.08885341,0.039053302,-0.015262977,-0.031253684,0.03417885,0.071181856,-0.007808616,0.12355669,0.021872463,-0.07052631,0.034643795,-0.009103888,0.0009992219,-0.034064244,0.023540951,-0.011544353,0.044490743,0.012196002,0.06250982,0.032432035,-0.020601276,0.033151444,0.049982004,-0.0046420014,0.01634675,-0.03043463,-0.022835959,0.10335953,-0.024537504,-0.013943072,-0.037675563,-0.013128811,0.03696739,-0.012703919,-0.038263682,0.05135226,-0.012949898,0.03779803,-0.017548248,0.0075954134,-0.05095444,0.02818164,0.03148827,-0.0164495,0.032017045,-0.049015086,-0.036766473,-0.0018391924,-0.079134196,0.022092553,-0.051675618,-0.0015108358,0.004532138,-0.028692901,-0.015243589,0.05416649,0.03366958,-0.053588536,-0.030014247,-0.1531701,0.017888602,-0.03791488,0.05584656,-0.046475917,-0.020193826,-0.07300534,-0.0047246874,-0.059161738,0.066732064,0.0790493,-0.016203035,-0.0027307004,-0.0020972684,0.0064643654,-0.046132956,0.043391183,0.016732967,0.02703182,0.007972792,0.057761747,-0.008852981,0.021252126,0.02475415,-0.030986307,-0.020247025,-0.09130176,-0.04606675,0.044885874,0.060445506,-0.06706025,-0.022632452,-0.015277824,0.04688439,-0.04723752,0.03209871,0.021821171,0.08922093,0.0017031011,0.045463733,0.104772836,-0.064984545,-0.06575538,-0.0033132911,-0.022468958,0.025835639,-0.052615922,-0.033846986,0.029656392,-0.02030669,-0.0035152533,-0.014226459,-0.042199764,-0.05230265,0.04099582,-0.032932293,0.011331562])
# vec3 = np.array([0.040464643,-0.105283305,-0.032927666,0.08482682,-0.008149427,-0.015940541,0.011386896,0.057241183,0.0070870025,-0.04212644,0.016014865,0.046910495,0.050700583,0.04713082,0.022175903,0.017228305,-0.029237255,-0.048329853,-0.050303023,-0.032257825,-0.011404074,0.045193557,0.0031712947,-0.010680897,0.050225936,-0.08708012,0.024471255,-0.00094653014,-0.023796592,0.033517987,-0.12896886,-0.031903952,0.017394155,-0.022211045,-0.020303488,0.03654168,-0.0106786955,0.007375446,0.00525742,0.03497844,0.015308204,0.024407854,-0.0010341142,-0.014596779,-0.011007236,0.023385668,0.007930365,0.0010320271,0.043266952,-0.03199141,0.07671391,-0.0692293,-0.018234886,0.037217822,-0.13965589,-0.06807823,-0.019081477,-0.0056295497,0.0013769252,-0.02319661,0.040761847,-0.060449272,0.05701828,0.005460848,0.035557646,0.0035891873,0.013037635,0.028751966,-0.013681242,0.041959472,-0.068879224,0.049196,-0.04060982,0.061983857,0.0032824592,-0.047742598,-0.0704569,-0.017971754,0.013160182,-0.05507056,-0.010865227,-0.028084368,-0.015340036,0.015320436,0.04229507,-0.028918887,-0.096728794,0.04519577,-0.058505535,-0.020383408,0.014328574,0.008358328,-0.055293757,0.043947544,-0.06921587,-0.026566545,-0.0059614372,0.024782334,-0.008290632,0.02867329,0.054857705,0.044260617,0.004816123,-0.011475204,0.016317839,0.005502515,-0.01073339,-0.036409806,0.00932517,0.0010854503,-0.06089302,-0.037443317,0.009429939,-0.0149351945,-0.037973534,-0.0625554,-0.0091355145,0.010780921,-0.037742384,0.008262036,0.058859106,0.021872949,-0.023779968,0.07089992,0.02610335,0.017279334,-0.0021878846,-0.012223247,-0.012126642,0.03219317,-0.0066032223,0.035348177,-0.020562911,-0.021436667,0.045531902,0.0982004,-0.05514105,0.067004375,-0.063074306,0.018825727,0.047909763,0.0060998863,0.058173433,0.020530507,0.016158963,0.04174406,0.02003265,0.016958745,0.0033393959,-0.043342173,0.0023003693,-0.050927453,0.24582101,0.011927499,-0.033813506,0.00030503084,0.03536795,0.070579596,0.011295102,-0.027774358,0.037635047,0.01983737,0.011734145,0.04698608,0.037603848,0.010704102,-0.029094331,-0.013851285,0.029247811,0.000013736222,-0.026923453,0.02281319,0.046900876,0.0019288617,0.061410766,0.0035797302,0.016855383,0.03896088,-0.0073125036,0.02866458,0.059646714,-0.00068961363,0.042542942,0.048288826,-0.039733544,-0.031042013,-0.044311397,0.019716393,0.012234813,-0.07952621,0.031486806,0.03919334,-0.0024836024,-0.05096016,0.0002857223,0.0026416178,-0.030441415,-0.041867223,-0.013386491,0.02529168,-0.019947633,-0.05091116,0.068082206,0.004328997,0.0060102562,-0.0071535483,0.033404876,0.0052697873,0.02829395,-0.015224372,0.008231803,0.04761694,0.006811485,0.00054063665,0.027975695,0.02508009,0.014651712,-0.030757798,0.009152641,0.07094154,0.044850133,-0.015637299,0.03199977,-0.030060876,0.018757919,0.058616042,-0.03980826,0.030871963,0.010339103,0.016877003,0.0048178174,0.02787026,-0.043410838,-0.043274593,0.02378993,-0.0020224566,0.04323649,0.020181112,0.03101712,-0.01065249,-0.055999372,0.01604417,0.015821602,0.029431151,0.009957514,-0.051102977,0.09628327,0.014154248,-0.032628436,0.03663614,-0.024510896,0.03333631,0.02594363,-0.06885442,-0.031838182,-0.036416095,-0.05033359,-0.05776682,0.051239986,0.040093593,-0.005359583,-0.056177434,0.037931066,0.0022929932,0.05113335,-0.008139679,-0.01716167,-0.022418255,-0.029251833,0.010584377,-0.098869786,0.005083074,0.03948035,-0.051378306,0.030420193,0.015110974,-0.0006975726,-0.0068933107,0.034217265,-0.06802532,-0.0112210065,0.0314844,0.03198802,0.04972025,0.029684259,-0.04931148,-0.03258505,0.023569413,-0.024090448,-0.00091811264,-0.068983845,0.012029351,0.090343274,-0.045988653,-0.03322181,0.030121082,-0.02350668,-0.04207414,0.013512837,0.039588235,-0.07619595,0.028745705,-0.06092207,-0.042524688,-0.0247878,-0.02509094,0.041109543,-0.24503586,-0.011575019,-0.0313846,0.04005226,0.11059323,-0.06117207,0.013063294,0.011205132,0.046260327,-0.0635677,-0.030855978,-0.005286718,-0.121757224,0.0013309186,0.02800644,-0.047652625,-0.0018397282,-0.15588135,-0.029369907,0.099838614,-0.024229635,0.053455204,0.0008232326,0.046104353,-0.010305262,0.008213524,0.059844047,0.048355393,-0.0010148919,-0.041439354,-0.028392565,0.034008715,-0.073668234,-0.017207123,0.009783124,0.002533115,0.010221574,0.025113901,0.044531405,-0.008413104,-0.06375541,-0.13371024,-0.033283103,0.086862385,0.0052239792,-0.017458728,-0.043836802,-0.038732104,0.009043836,0.03548021,0.058956098,-0.012917142,0.010555311,0.030476108,-0.021277718,-0.052135613,0.043352373,-0.0027770095,-0.008285178,-0.0027227607,0.038835052,-0.0639556,-0.06514385,-0.01664987,0.03236255,0.02938306,-0.03952446,0.07174268,0.061922185,-0.014581832,0.016359333,-0.062135477,0.002994568,0.0035710477,0.066198,0.060568642,0.010397144,-0.01840087,0.09294149,-0.004763685,-0.0138351405,0.021309735,0.008374671,0.014978127,0.004400897,0.020547373,-0.058334626,-0.031508192,0.021595726,-0.05959455,0.00781582,0.015893644,0.023015542,0.019572923,0.011664829,-0.03320624,0.09414911,0.020662524,0.049060248,0.02774912,0.042882632,-0.0073423283,-0.033388782,0.035855826,-0.07333014,0.040190052,0.008850699,0.044222165,-0.014860667,0.015795741,0.050199278,-0.013068834,0.013066839,0.037643857,-0.017648678,-0.05748757,0.014155486,0.0012556809,0.0019725794,-0.03801218,0.02929353,0.009696242,-0.041440386,0.015847053,0.017184466,0.00961586,0.011837683,-0.01687195,0.020328052,-0.029413346,-0.018626524,0.054167222,-0.036621742,-0.07322093,-0.0019500018,-0.060578626,-0.04192094,-0.0182675,-0.049628537,-0.0023824447,-0.044502504,-0.0007070397,0.018204143,0.069282435,0.006634703,0.011974619,-0.013050559,0.00416978,-0.10211305,-0.015774403,-0.03187088,0.006348435,-0.031723235,0.11897235,-0.034866676,0.028345753,-0.03392262,0.0681197,-0.0017426745,0.017155409,0.038920257,-0.0421618,0.027482755,0.0015424307,0.09056142,-0.031602874,0.049377054,0.021309774,0.10232258,-0.03529787,-0.02464906,0.03714182,0.032786634,-0.034073304,-0.10074513,0.022511218,0.02179045,0.014811261,-0.05228692,-0.09407746,0.056029465,0.043751717,-0.0015979314,-0.07361951,-0.015016706,0.07677145,0.06421322,0.0033711484,0.081782624,-0.0372505,-0.065752976,-0.069149695,-0.026542079,-0.011239862,-0.010664053,-0.012738289,0.036829475,0.065496154,-0.019801777,-0.031489726,0.036589574,0.010882895,0.054022834,-0.035650685,-0.013580029])

# # 1. Qdrant’a bağlan
# client = QdrantClient(host="localhost", port=6333)

# # 2. Koleksiyon oluştur
# collection_name = "MarkaCollection"
# vector_size = 512  # CLIP embedding boyutu

# # Koleksiyon var mı kontrol et, yoksa oluştur
# if not client.collection_exists(collection_name=collection_name):
#     client.create_collection(
#         collection_name=collection_name,
#         vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
#     )

# try:
#     # Görselden embedding çıkar
#     vector = calculate_mean_vector(vec1, vec2, vec3)
    
#     # Ürün bilgisi ve kategorik yapı
#     metadata = {
#         "product_name": "Sutas",
#         "categories": ["Gıda", "Marka", "Sutas"]
#     }

#     # Qdrant’a ekle
#     point = PointStruct(
#         id=str(uuid.uuid4()),  # Her ürün için benzersiz ID oluştur
#         vector=vector,  # Görselin embedding’i
#         payload=metadata  # Kategorik ve diğer bilgileri içerir
#     )

#     # Veriyi Qdrant’a yükle
#     client.upsert(collection_name=collection_name, points=[point])
#     print(f"{vector} yüklendi.")

# except Exception as e:
#     print(f"Hata oluştu: {vector} - {e}")

"""
    # gorsel embedding'lerinin ortalamasini alarak test
    
"""


# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct
# import os
# import uuid
# import numpy as np
# from embedding_model import get_embedding

# # 1. Qdrant’a bağlan
# client = QdrantClient(host="localhost", port=6333)

# # 2. Koleksiyon oluştur
# collection_name = "sutas_icim_embed_mean"
# vector_size = 512  # CLIP embedding boyutu

# # Eğer koleksiyon yoksa, oluştur
# if not client.collection_exists(collection_name=collection_name):
#     client.create_collection(
#         collection_name=collection_name,
#         vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
#     )

# # client.create_collection(
# #     collection_name=collection_name,
# #     vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
# # )

# # 3. Alt klasörlerdeki tüm .jpeg dosyaları için işlemi yap
# image_folder = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/sutas-icim/icim"

# for root, _, files in os.walk(image_folder):
#     # Her klasör için embedding'leri saklamak için bir liste
#     embeddings = []
#     folder_name = os.path.basename(root)  # Klasör adı (ürün adı gibi)

#     for file in files:
#         if file.endswith(".jpeg"):
#             full_path = os.path.join(root, file)
#             try:
#                 # Görselin embedding'ini çıkar
#                 vector = get_embedding(full_path)
#                 embeddings.append(vector)
#                 print(f"{full_path} için embedding çıkarıldı.")
#             except Exception as e:
#                 print(f"Hata oluştu: {file} - {e}")

#     # Eğer klasörde embedding varsa, ortalama embedding'i hesapla
#     if embeddings:
#         # NumPy kullanarak ortalama embedding'i hesapla
#         average_embedding = np.mean(embeddings, axis=0)

#         # Ortalama embedding'i Qdrant'a yükle
#         metadata = {
#             "folder": folder_name,  # Hangi klasör (ürün) için olduğunu belirt
#             "type": "icim_embedding"  # Bu bir ortalama embedding
#         }
#         point = PointStruct(
#             id=str(uuid.uuid4()),
#             vector=average_embedding.tolist(),
#             payload=metadata
#         )
#         client.upsert(collection_name=collection_name, points=[point])
#         print(f"{folder_name} için ortalama embedding yüklendi.")

"""
    # gorsel embedding'lerinin Cosine Similarity alarak test
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import os
import uuid
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embedding_model import get_embedding

# 1. Qdrant’a bağlan
client = QdrantClient(host="localhost", port=6333)

# 2. Koleksiyon oluştur
collection_name = "sutas_icim_embed_mean"
vector_size = 512  # CLIP embedding boyutu

# Eğer koleksiyon yoksa, oluştur
if not client.collection_exists(collection_name=collection_name):
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )

# 3. Alt klasörlerdeki tüm .jpeg dosyaları için işlemi yap
image_folder = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/products"

for root, _, files in os.walk(image_folder):
    # Her klasör için embedding'leri saklamak için bir liste
    embeddings = []
    folder_name = os.path.basename(root)  # Klasör adı (ürün adı gibi)

    for file in files:
        if file.endswith(".jpeg", "jpg", "png"):
            full_path = os.path.join(root, file)
            try:
                # Görselin embedding'ini çıkar
                vector = get_embedding(full_path)
                embeddings.append(vector)
                print(f"{full_path} için embedding çıkarıldı.")
            except Exception as e:
                print(f"Hata oluştu: {file} - {e}")

    # Eğer klasörde embedding varsa, en temsili embedding'i seç
    if embeddings:
        # Embedding'ler arasındaki cosine similarity matrisini hesapla
        similarity_matrix = cosine_similarity(embeddings)

        # Her embedding'in diğer embedding'lere olan benzerliklerinin ortalamasını al
        similarity_scores = similarity_matrix.mean(axis=1)

        # En yüksek benzerlik skoruna sahip embedding'i seç
        most_representative_index = np.argmax(similarity_scores)
        most_representative_embedding = embeddings[most_representative_index]

        # Temsili embedding'i Qdrant'a yükle
        metadata = {
           
        }
        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=most_representative_embedding.tolist(),
            payload=metadata
        )
        client.upsert(collection_name=collection_name, points=[point])
        print(f"{folder_name} için temsili embedding yüklendi.")



"""
    hiyerarsik yukleme
"""

# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct
# import os
# import uuid
# import numpy as np
# from embedding_model import get_hierarchical_embedding  # Hierarchical modeli kullandığımızı unutma!

# # 1. Qdrant’a bağlan
# client = QdrantClient(host="localhost", port=6333)

# # 2. Koleksiyon oluştur
# collection_name = "sutas_icim_hierarchical"
# vector_size = 512  # CLIP embedding boyutu

# if not client.collection_exists(collection_name=collection_name):
#     client.create_collection(
#         collection_name=collection_name,
#         vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
#     )

# # 3. Kategori ve Ürün Adı eşleşmelerini tanımla
# mapping = {
#     "SüzmePeynir": {
#         "categories": ["Gıda", "icim", "Peynir"],
#         "product_name": "icim-tag-yagli-peynir-500Gr"
#     },
#     # Yeni ürünleri buraya ekle
# }

# # 4. Görsellerin bulunduğu üst klasör
# image_folder = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Gıda/icim/Peynir/SüzmePeynir"

# for root, _, files in os.walk(image_folder):
#     folder_name = os.path.basename(root)  # ürün adı (klasör adı)

#     # Eğer klasör mapping içinde yoksa atla
#     if folder_name not in mapping:
#         print(f"Mapping bulunamadı: {folder_name}, atlanıyor...")
#         continue

#     embeddings = []

#     for file in files:
#         if file.endswith(".jpg"):
#             full_path = os.path.join(root, file)
#             try:
#                 vector = get_hierarchical_embedding(
#                     image_path=full_path,
#                     category_list=mapping[folder_name]["categories"],
#                     product_name=mapping[folder_name]["product_name"]
#                 )
#                 embeddings.append(vector)
#                 print(f"{full_path} için embedding çıkarıldı.")
#             except Exception as e:
#                 print(f"Hata oluştu: {file} - {e}")

#     if embeddings:
#         average_embedding = np.mean(embeddings, axis=0)

#         metadata = {
#             "folder": folder_name,
#             "categories": mapping[folder_name]["categories"],
#             "product_name": mapping[folder_name]["product_name"],
#             "type": "hierarchical_embedding"
#         }

#         point = PointStruct(
#             id=str(uuid.uuid4()),
#             vector=average_embedding.tolist(),
#             payload=metadata
#         )
#         client.upsert(collection_name=collection_name, points=[point])
#         print(f"{folder_name} için ortalama embedding yüklendi.")

# from qdrant_client import QdrantClient
# from qdrant_client.models import Distance, VectorParams, PointStruct
# import numpy as np
# import uuid

# # 1. Qdrant’a bağlan
# client = QdrantClient(host="localhost", port=6333)

# # 2. Ortalama vektörü hesapla ve yeni koleksiyona yükle
# def mean_vector_to_new_collection(source_collections, new_collection_name, payload_label):
#     all_vectors = []

#     # Her koleksiyondan vektörleri çek
#     for collection in source_collections:
#         scroll_result = client.scroll(
#             collection_name=collection,
#             limit=1000,
#             with_vectors=True
#         )
#         vectors = [point.vector for point in scroll_result[0]]
#         if len(vectors) > 0:
#             all_vectors.append(np.array(vectors))
#             print(f"{collection}: {len(vectors)} vektör alındı.")
#         else:
#             print(f"⚠️ {collection} koleksiyonunda vektör yok.")

#     if not all_vectors:
#         print("❌ Hiç vektör bulunamadı.")
#         return

#     # Vektörleri birleştirip ortalama al
#     combined_vectors = np.vstack(all_vectors)
#     mean_vector = np.mean(combined_vectors, axis=0)

#     # Eski koleksiyon varsa sil
#     if client.collection_exists(collection_name=new_collection_name):
#         client.delete_collection(collection_name=new_collection_name)
#         print(f"🗑 {new_collection_name} koleksiyonu silindi.")

#     # Yeni koleksiyon oluştur
#     vector_size = len(mean_vector)
#     client.create_collection(
#         collection_name=new_collection_name,
#         vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
#     )
#     print(f"📦 Yeni koleksiyon oluşturuldu: {new_collection_name}")

#     # Tek vektör olarak yükle
#     point = PointStruct(
#         id=str(uuid.uuid4()),
#         vector=mean_vector.tolist(),
#         payload={
#             "label": payload_label,
#             "source_collections": source_collections
#         }
#     )
#     client.upsert(collection_name=new_collection_name, points=[point])
#     print(f"✅ Ortalama vektör yüklendi: {new_collection_name}")

# # === Kullanım örneği ===
# mean_vector_to_new_collection(
#     source_collections=["icim_peynir", "icim_sut", "icim_puding"],
#     new_collection_name="icim_kategori_mean",
#     payload_label="icim_mean"
# )




# Gerekli kütüphaneler
# import os
# import torch
# import numpy as np
# from PIL import Image
# from transformers import CLIPProcessor, CLIPModel
# from qdrant_client import QdrantClient
# from qdrant_client.models import PointStruct, VectorParams, Distance

# # 1. CLIP modelini yükle (görselleri vektöre dönüştürmek için kullanıyoruz)
# device = "cuda" if torch.cuda.is_available() else "cpu"  # GPU varsa kullan
# model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip").to(device)
# processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")

# # 2. Qdrant veritabanı bağlantısını kur
# client = QdrantClient(host="localhost", port=6333)

# # 4. Ürün ID'lerine göre kategori ve alt kategori eşlemesi (senin gönderdiğin tabloya göre)
# kategori_mapping = {
#     "tekel": {
#         "sigaraTekel": [1, 2],
#         "alkolTekel": [14, 15]
#     },
#     "gida": {
#         "icecekGida": {
#             "meyvesuyuIcecekGida": [50, 51],
#             "suIcecekGida": [92, 95],
#             "SutIcecekGida": [1964, 1965],
#         },
#         "yiyecekGida": [358, 359]
#     },
#     "temizlik": {
#         "bebekTemizlik ": [1974, 1975],
#         "evTemizlik": [855, 856],
#         "kisiselBakimTemizlik": [25, 26]
#     }
# }

# def find_kategori_by_id(urun_id):
#     for kategori, altlar in kategori_mapping.items():
#         for alt_kategori, id_list in altlar.items():
#             if isinstance(id_list, list):  # alt_kategori doğrudan listeyse
#                 if urun_id in id_list:
#                     return kategori, alt_kategori
#             elif isinstance(id_list, dict):  # bir alt-alan sözlüğü varsa
#                 for sub_kategori, sub_ids in id_list.items():
#                     if urun_id in sub_ids:
#                         return kategori, sub_kategori
#     return None, None

# def get_image_vector(image_path):
#     try:
#         image = Image.open(image_path).convert("RGB")
#         inputs = processor(images=image, return_tensors="pt").to(device)
#         with torch.no_grad():
#             features = model.get_image_features(**inputs)
#         return features[0].cpu().numpy()
#     except:
#         return None

# base_path = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/products"

# # Tüm kategori temsil vektörleri burada tutulacak
# kategori_vectors = {}

# for urun_id in os.listdir(base_path):
#     urun_path = os.path.join(base_path, urun_id)
#     if not os.path.isdir(urun_path):
#         continue

#     # Sadece sayıya çevrilebilen dizin adlarını işle
#     try:
#         urun_id_int = int(urun_id)
#     except ValueError:
#         print(f"Aşılan klasör (skip): {urun_id}")
#         continue

#     kategori, alt_kategori = find_kategori_by_id(urun_id_int)

#     collection_name = f"{kategori}_{alt_kategori}"
#     collection_name = collection_name.lower()

#     # Eğer koleksiyon yoksa oluştur
#     if collection_name not in [c.name for c in client.get_collections().collections]:
#         client.create_collection(
#             collection_name=collection_name,
#             vectors_config=VectorParams(size=512, distance=Distance.COSINE)
#         )

#     vectors = []
#     for img_file in os.listdir(urun_path):
#         if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
#             vec = get_image_vector(os.path.join(urun_path, img_file))
#             if vec is not None:
#                 vectors.append(vec)

#     if vectors:
#         mean_vector = np.mean(vectors, axis=0)

#         # Ürünü koleksiyonuna yükle
#         client.upsert(
#             collection_name=collection_name,
#             points=[
#                 PointStruct(
#                     id=int(urun_id),
#                     vector=mean_vector.tolist(),
#                     payload={"urun_id": urun_id}
#                 )
#             ]
#         )

#         print(f"Yüklendi: {urun_id} → {collection_name}")

#         # Bu vektörü kategori ortalaması için sakla
#         if kategori not in kategori_vectors:
#             kategori_vectors[kategori] = []
#         kategori_vectors[kategori].append(mean_vector)

# # 🔁 En sonunda: Her kategori için üst seviye temsil vektörü üret ve ayrı koleksiyona koy
# for kategori, vectors in kategori_vectors.items():
#     ortalama = np.mean(vectors, axis=0)
#     ust_koleksiyon = f"{kategori}_temsil"
#     ust_koleksiyon = ust_koleksiyon.lower()

#     if ust_koleksiyon not in [c.name for c in client.get_collections().collections]:
#         client.create_collection(
#             collection_name=ust_koleksiyon,
#             vectors_config=VectorParams(size=512, distance=Distance.COSINE)
#         )

#     client.upsert(
#         collection_name=ust_koleksiyon,
#         points=[
#             PointStruct(
#                 id=0,
#                 vector=ortalama.tolist(),
#                 payload={"kategori": kategori}
#             )
#         ]
#     )
#     print(f"Kategori temsili yüklendi: {kategori} → {ust_koleksiyon}")