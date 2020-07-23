import streamlit as st

#importando as bibliotecas e dataframe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#from bokeh.plotting import figure
from pylab import *
import joblib
import os
from PIL import Image
#import pandas_bokeh


#DataBase
DATA_PATH = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(DATA_PATH)

#Programa Principal
def main():
    st.title("COVID-19")
    st.sidebar.title('Menú COVID-19')
    add_selectbox = st.sidebar.selectbox('Por favor, selecciona una opción: ',('Principal', 'Análisis Exploratorio por País', 'Análisis Exploratorio a Nivel Mundial'))
    ##NUEVO MENU: PRINCIPAL
    if add_selectbox == 'Principal':
        st.header('Introducción al COVID-19')
        st.write('Coronavirus y Nuevo Coronavirus son los nombres de los virus, y CoViD-19 es el nombre de la enfermedad  causada por el Nuevo Coronavirus. Identificados en la década de 1960, los Coronavirus pertenecen a la  subfamilia taxonómica Orthocoronavirinae de la familia Coronaviridae, del orden Nidovirales.  Se subdividen en varios géneros, especies y cepas. Algunos atacan a los animales, otros afectan a la  especie humana, causando desde enfermedades leves con síntomas similares a un resfriado común, hasta enfermedades graves como el SARS, el MERS y el actual CoViD-19.')
        st.write('El coronavirus se dio a conocer en todo el mundo en 2002 cuando causó el Síndrome Respiratorio Agudo Severo (SARS), una enfermedad que se propagó a varios países desde China, causando alrededor de 800 víctimas, el 10% de las 8000 personas que se infectaron. Una nueva cepa de coronavirus, que apareció en Jordania en 2012, causó el Síndrome Respiratorio del Medio Oriente (MERS), una enfermedad que se propagó en el Medio Oriente y llegó a Corea del Sur, matando al 35% de las 2500 personas infectadas, una enfermedad que mostró una impresionante tasa de letalidad del 35%. Y en China, en 2019, surgió otra cepa del virus, el Nuevo Coronavirus, responsable de la enfermedad CoViD-19 que está causando esta pandemia. Su tasa de mortalidad es del 3 al 4%, pero su capacidad de transmisión es mucho mayor que la de otros virus, ya que se transmite incluso por personas sin ningún tipo de síntomas y tiene una capacidad y velocidad de reproducción mucho más altas que las de otros virus.')
        st.header('¿Qué es COVID-19?')
        st.write('COVID-19 es una enfermedad causada por el coronavirus SARS-CoV-2, que presenta un cuadro clínico que abarca desde infecciones asintomáticas hasta afecciones respiratorias graves. Según la Organización Mundial de la Salud (OMS), la mayoría de los pacientes con COVID-19 (aproximadamente el 80%) pueden ser asintomáticos y aproximadamente el 20% de los casos pueden requerir atención hospitalaria porque tienen dificultad para respirar y de estos casos aproximadamente el 5% puede necesitar apoyo para el tratamiento de la insuficiencia respiratoria (respirador artificial)')
        st.subheader('¿Qué es el coronavirus?')
        st.write('El coronavirus es una familia de virus que causan infecciones respiratorias. El nuevo agente de coronavirus fue descubierto el 31/12/19 después de los casos registrados en China. Causa la enfermedad llamada coronavirus (COVID-19). Los primeros coronavirus humanos se aislaron por primera vez en 1937. Sin embargo, fue en 1965 que el virus se describió como coronavirus, debido al perfil bajo microscopía, que parecía una corona. La mayoría de las personas se infectan con coronavirus comunes a lo largo de sus vidas, y los niños pequeños tienen más probabilidades de infectarse con el tipo más común del virus. Los coronavirus más comunes que infectan a los humanos son el coronavirus alfa 229E y NL63 y el coronavirus beta OC43, HKU1.')
        st.header('Síntomas')
        st.write('Los síntomas de COVID-19 pueden variar desde un simple resfriado hasta una neumonía grave. Los síntomas más comunes son: Tos, Fiebre, Rinitis, Dolor de garganta, Dificultades respiratorias')
        st.header('Transmisión')
        st.write('La transmisión ocurre de una persona enferma a otra o por contacto cercano a través de: Toque o apretón de manos; Gotitas de saliva; Estornudo; Tos; Catarro; Objetos o superficies contaminadas, como teléfonos celulares, mesas, manijas de puertas, juguetes, teclados de computadora, etc.')
        st.header('Fuente de los Datos')
        st.write('Los datos fueron tomados de Github de OurWorldInData, que es una organización sin fines de lucro que recopila y proporciona datos gratuitos sobre "pobreza, enfermedad, hambre, cambio climático, guerra, riesgos existenciales y desigualdad". Los datos mundiales sobre Covid-19 son actualizados diariamente por la organización, que es una de las más respetadas en el mundo en relación con el suministro de datos. Puede acceder a estos datos públicos actualizados aquí.')
        st.markdown("[OurWorldInData](https://ourworldindata.org/)")
        
        st.header('Biblioteca')
        st.write('Comprender los datos es tan importante como el análisis exploratorio, porque si no se comprende lo que significa y de dónde provienen los datos, no se podrá realizar un análisis completo.')
        #Datos tabla
        informacion = {'Descripción':['Letras y códigos de los países en base a ISO 3166-1 alpha-3', 'Continente', 'Localización Geográfica', 'Fecha de Observación','Total de Casos Confirmados de COVID19','Nuevos Casos Confirmados de COVID19','Total de Muertes Atribuídas al COVID19','Nuevas Muertes Atribuídas al COVID19','Total de Casos Confirmados de COVID19 por millón de habitantes','Nuevos Casos Confirmados de COVID19 por millón de habitantes','Total de Muertes Atribuídas al COVID19 por millón de habitantes','Nuevas Muertes Atribuídas al COVID19 por millón de habitantes','Total de Pruebas para COVID19','Nuevas Pruebas para COVID19','Nuevas Pruebas de COVID19 (suavizado por 7 dias)','Total de Pruebas de COVID19 por 1000 habitantes','Nuevas Pruebas de COVID19 por 1000 habitantes','Nuevas Pruebas de COVID19 (suavizado por 7 dias) por 1000 habitantes','Unidades usadas para informar datos de pruebas','Indice de Respuesta del Gobierno','Población en 2020','Densidad demográfica (en km cuadrados)','Média de Edad de la Población','Proporción de la población con 65 años o más','Proporción de la población con 70 años o más','PIB a la par con el poder de compra (dólares internacionales constantes de 2011)','Porcentaje de la población que vive en extrema pobreza, año más reciente desde 2010','Tasa de mortalidad por enfermedades cardiovasculares en 2017','Prevalencia de diabetes (% de población entre 20 y 79 años) en 2017', 'Porcentaje de mujeres que fuman','Porcentaje de hombres que fuman','Porcentaje de la población con instalaciones básicas de lavado de manos en las instalaciones, en el último año disponible','Camas de hospital por cada 1,000 personas, último año disponible desde 2010','Esperanza de vida al nacer en 2019'],
                       'Origen':['International Organization for Standardization','Our World in Data','Our World in Data','Our World in Data','Centro Europeo para la Prevención y el Control de Enfermedades','Centro europeo para la prevención y el control de enfermedades','Centro europeo para la prevención y el control de enfermedades','Centro europeo para la prevención y el control de enfermedades','Centro europeo para la prevención y el control de enfermedades','Centro europeo para la prevención y el control de enfermedades','Centro europeo para la prevención y el control de enfermedades','Centro europeo para la prevención y el control de enfermedades','National government reports','National government reports','National government reports','National government reports','National government reports','National government reports','National government reports','	Oxford COVID-19 Government Response Tracker, Blavatnik School of Government','United Nations','World Bank','UN Population Division','Banco Mundial','Naciones Unidas, Departamento de Asuntos Económicos y Sociales, División de Población (2017)','	Banco Mundial','	Banco Mundial','Red Global Colaborativa de Carga de Enfermedades','	Banco Mundial','	Banco Mundial','	Banco Mundial','División de Estadística de las Naciones Unidas','OCDE, Eurostat, Banco Mundial, registros del gobierno nacional y otras fuentes','James C. Riley, Clio Infra, División de Población de las Naciones Unidas']}
        df_info = pd.DataFrame(informacion, columns=['Descripción','Origen'])
        df_info = pd.DataFrame(informacion, columns=['Descripción','Origen'],index=df.columns)
        st.table(df_info)
        st.subheader("Base de Datos del COVID19 mostrando los 5 primeras filas")
        #Transformar la columna "date" no formato datetime
        df.date = pd.to_datetime(df.date)
        df.date.max()
        df.set_index('date', inplace=True)
        st.dataframe(df[df.location=='World'].head(5))
        #Description
        if st.checkbox("Mostrar Descripcion de la Base de Datos"):
            st.write(df.describe())
        #Shape
        if st.checkbox("Mostrar Dimensiones de la Base de Datos"):
            st.write(df.shape)
            data_dim = st.radio("Mostrar Dimensiones por: ",("Filas", "Columnas"))
            if data_dim == "Filas":
                st.write("Numero de Filas: ")
                st.write(df.shape[0])
            elif data_dim == "Columnas":
                st.write("Numero de Columnas: ")
                st.write(df.shape[1])
        #Correlacion
        st.header("Correlación")
        st.write("La correlación indica la fuerza y la dirección de una relación lineal y proporcionalidad entre dos variables estadísticas.")
        columnas = df.columns#Una lista con las columnas
        st.info("El siguiente mapa de calor representa una correlación visual, que varía de -1 a 1, donde -1 se considera sin correlación y 1 se considera una correlación perfecta.")        
        columnas_seleccionadas = st.multiselect("Selecciona las columnas para generar el mapa de correlacion: " , columnas)
        if len(columnas_seleccionadas) > 0:
            correlacion = df[columnas_seleccionadas].corr()
            fig, ax = plt.subplots(figsize=(12,12))
            st.write(sns.heatmap(correlacion,annot=True, fmt='.2f', ax=ax, square=True))
            st.pyplot()





        
        
        
        st.success('En el Menú Lateral Puedes Seleccionar y Empezar con el Análisis Exploratorio del COVID-19')
        
        
        
        st.write("Desarrollado por: Juan Minango, David Minango y Rafael Bolsoni")
        st.markdown("[JD-TECHN](https://jdtechn.com/)")
        st.write("Con el auspicio de:")
        st.markdown("[Capacitate Ecuador](https://www.facebook.com/Capacitate.Ecu/)")
        
    ##NUEVO MENU: ANALISIS EXPLORATORIO POR PAIS
    elif add_selectbox == 'Análisis Exploratorio por País':
        #Transformar la columna "date" no formato datetime
        st.header("Análisis Exploratorio por País")
        df.date = pd.to_datetime(df.date)
        df.date.max()
        df.set_index('date', inplace=True)
        #Seleccion de Paises
        list_paises = df.location.unique()
        paises = st.selectbox("Escoja el Pais",list_paises)
        paises_df = df[df['location'].str.contains(paises)]
        countries_images = {'af': 'Afghanistan','al': 'Albania','dz': 'Algeria','as': 'American Samoa','ab':'Antigua and Barbuda','ad': 'Andorra','ao': 'Angola','ai': 'Anguilla','aq': 'Antarctica','ag': 'Antigua And Barbuda','ar': 'Argentina','am': 'Armenia','aw': 'Aruba','au': 'Australia','at': 'Austria','az': 'Azerbaijan','bs': 'Bahamas','bh': 'Bahrain','bd': 'Bangladesh','bb': 'Barbados','by': 'Belarus','be': 'Belgium','bz': 'Belize','bj': 'Benin','bm': 'Bermuda','bt': 'Bhutan','bo': 'Olivia','ba': 'Bosnia and Herzegovina','bw': 'Botswana','bv': 'Bouvet Island','br': 'Brazil','io': 'British Indian Ocean Territory','bn': 'Brunei','bg': 'Bulgaria','bf': 'Burkina Faso','bi': 'Burundi','kh': 'Cambodia','cm': 'Cameroon','ca': 'Canada','cv': 'Cape Verde','ky': 'Cayman Islands','cf': 'Central African Republic','td': 'Chad','cl': 'Chile','cn': 'China','cx': 'Hristmas Island','cc': 'Cocos (Keeling) Islands','co': 'Colombia','km': 'Comoros','cg': 'Congo','cd': 'Democratic Republic of Congo','ck': 'Cook Islands','cr': 'Costa Rica','ci': "Cote d'Ivoire",'hr': 'Croatia','cu': 'Cuba','cy': 'Cyprus','cz': 'Czech Republic','dk': 'Denmark','dj': 'Djibouti','dm': 'Dominica','do': 'Dominican Republic','ec': 'Ecuador','eg': 'Egypt','eh': 'Western Sahara','sv': 'El Salvador','gq': 'Equatorial Guinea','er': 'Eritrea','ee': 'Estonia','et': 'Ethiopia','fk': 'Falkland Islands','fo': 'Aroe Islands','fj': 'Fiji','fi': 'Finland','fr': 'France','gf': 'French Guiana','pf': 'French Polynesia','tf': 'French Southern Territories','ga': 'Gabon','gm': 'Gambia','ge': 'Georgia','de': 'Germany','gh': 'Ghana','gi': 'Gibraltar','gr': 'Greece','gl': 'Greenland','gd': 'Grenada','gp': 'Guadeloupe','gu': 'Guam','gt': 'Guatemala','gn': 'Guinea','gw': 'Guinea-Bissau','gy': 'Guyana','ht': 'Haiti','hm': 'Heard Island And Mcdonald Islands','hn': 'Honduras','hk': 'Hong Kong','hu': 'Hungary','is': 'Iceland','in': 'India','id': 'Indonesia','ir': 'Iran','iq': 'Iraq','ie': 'Ireland','il': 'Israel','it': 'Italy','jm': 'Jamaica','jp': 'Japan','jo': 'Jordan','kz': 'Kazakhstan','ke': 'Kenya','ki': 'Kiribati','kp': "Korea, Democratic People'S Republic Of",'kr': 'South Korea','kw': 'Kuwait','kg': 'Kyrgyzstan','la': 'Laos','lv': 'Latvia','lb': 'Lebanon','ls': 'Lesotho','lr': 'Liberia','ly': 'Libya','li': 'Liechtenstein','lt': 'Lithuania','lu': 'Luxembourg','mo': 'Macao','mk': 'Macedonia','mg': 'Madagascar','mw': 'Malawi','my': 'Malaysia','mv': 'Maldives','ml': 'Mali','mt': 'Malta','mh': 'Marshall Islands','mq': 'Martinique','mr': 'Mauritania','mu': 'Mauritius','yt': 'Mayotte','mx': 'Mexico','fm': 'Micronesia, Federated States Of','md': 'Moldova','mc': 'Monaco','mn': 'Mongolia','ms': 'Montserrat','ma': 'Morocco','mz': 'Mozambique','mm': 'Myanmar','na': 'Namibia','nr': 'Nauru','np': 'Nepal','nl': 'Netherlands','an': 'Netherlands Antilles','nc': 'New Caledonia','nz': 'New Zealand','ni': 'Nicaragua','ne': 'Niger','ng': 'Nigeria','nu': 'Niue','nf': 'Norfolk Island','mp': 'Northern Mariana Islands','no': 'Norway','om': 'Oman','pk': 'Pakistan','pw': 'Palau','ps': 'Palestine','pa': 'Panama','pg': 'Papua New Guinea','py': 'Paraguay','pe': 'Peru','ph': 'Philippines','pn': 'Pitcairn','pl': 'Poland','pt': 'Portugal','pr': 'Puerto Rico','qa': 'Qatar','re': 'Réunion','ro': 'Romania','ru': 'Russia','rw': 'Rwanda','sh': 'Saint Helena','kn': 'Saint Kitts and Nevis','lc': 'Saint Lucia','pm': 'Saint Pierre And Miquelon','vc': 'Saint Vincent and the Grenadines','ws': 'Samoa','sm': 'San Marino','st': 'Sao Tome and Principe','sa': 'Saudi Arabia','sn': 'Senegal','cs': 'Montenegro','sc': 'Seychelles','sl': 'Sierra Leone','sg': 'Singapore','sk': 'Slovakia','si': 'Slovenia','sb': 'Solomon Islands','so': 'Somalia','za': 'South Africa','gs': 'South Georgia And South Sandwich Islands','es': 'Spain','lk': 'Sri Lanka','sd': 'Sudan','sr': 'Suriname','sj': 'Svalbard And Jan Mayen','sz': 'Swaziland','se': 'Sweden','ch': 'Switzerland','sy': 'Syria','tw': 'Taiwan','tj': 'Tajikistan','tz': 'Tanzania','th': 'Thailand','tl': 'Timor','tg': 'Togo','tk': 'Tokelau','to': 'Tonga','tt': 'Trinidad and Tobago','tn': 'Tunisia','tr': 'Turkey','tm': 'Turkmenistan','tc': 'Turks and Caicos Islands','tv': 'Tuvalu','ug': 'Uganda','ua': 'Ukraine','ae': 'United Arab Emirates','gb': 'United Kingdom','us': 'United States','um': 'United States Minor Outlying Islands','uy': 'Uruguay','uz': 'Uzbekistan','ve': 'Venezuela','vu': 'Vanuatu','vn': 'Vietnam','vg': 'British Virgin Islands','vi': 'U.S. Virgin Islands','wf': 'Wallis And Futuna','ye': 'Yemen','zw': 'Zimbabwe','bl':'Bolivia','bonaire':'Bonaire Sint Eustatius and Saba','cura':'Curacao','faeroe':'Faeroe Islands','guy':'Guernsey','ilm':'Isle of Man','jey':'Jersey','ksv':'Kosovo','ser':'Serbia','sint':'Sint Maarten (Dutch part)','ssd':'South Sudan','usav':'United States Virgin Islands','vtc':'Vatican','zmb':'Zambia','wrl':'World','int':'International'}
        for k,v in countries_images.items():
            if v == paises:
                temp_images = 'cflags/{}.png'.format(k)
                #st.text(temp_images)
                img = Image.open(os.path.join(temp_images)).convert('RGB')
                st.image(img)
        st.dataframe(paises_df)
        st.subheader('Descripción de la Base de Datos:')
        st.dataframe(paises_df.describe())
        df_World = df[df['location'] == 'World'] #Total Mundial
        indice_World = df_World.index[-2] #El penuntilmo indice para asegurar
        #st.dataframe(df_World)
        #Graficos
        st.subheader('Gráficos Estadísticos de {}'.format(paises))
        if st.checkbox("Gráfico del Total de Casos y Muertes de COVID-19 en {}".format(paises)):
            df_temporal = pd.DataFrame({'Total_Casos' : []})
            df_temporal['Total_Casos'] = paises_df['total_cases']
            df_temporal['Total_Muertes'] = paises_df['total_deaths'] 
            st.line_chart(df_temporal,use_container_width=True)
        if st.checkbox("Gráfico de Nuevos Casos Diarios de COVID-19 en {}".format(paises)):
            df_temporal = pd.DataFrame({'Nuevos_Casos_Diarios' : []})
            df_temporal['Nuevos_Casos_Diarios'] = paises_df['new_cases']
            st.bar_chart(data=df_temporal,use_container_width=True)
        if st.checkbox("Gráfico de Nuevas Muertes Diarias de COVID-19 en {}".format(paises)):
            df_temporal = pd.DataFrame({'Nuevas_Muertes_Diarias' : []})
            df_temporal['Nuevas_Muertes_Diarias'] = paises_df['new_deaths'] 
            st.bar_chart(data=df_temporal,use_container_width=True)
        if st.checkbox("Gráfico de Tasa de Mortalidad de COVID-19 en {}".format(paises)):
            df_temporal = pd.DataFrame({'Tasa de Mortalidad' : []})
            df_temporal['Tasa de Mortalidad en %'] = (paises_df.total_deaths / paises_df.total_cases)*100
            st.bar_chart(data=df_temporal,use_container_width=True)    
        #EN COMPARACION AL MUNDO
        st.subheader('Gráficos Estadísticos de {} en Comparacion al Mundo'.format(paises))
        if st.checkbox("Gráfico del Total de Casos a Nivel Mundial y de {}".format(paises)):
            plt.plot(paises_df['total_cases'], label = 'Total de Casos {}'.format(paises))
            plt.plot(df_World['total_cases'], label = 'Total de Casos a Nivel Mundial')
            plt.yscale("log")
            plt.title('Escala Logaritmica')
            plt.ylabel('Cantidad')
            plt.xlabel('Fechas/Mes')
            plt.grid()
            plt.legend()
            st.pyplot()
        if st.checkbox("Gráfico del Total de Muertes a Nivel Mundial y de {}".format(paises)):
            plt.plot(paises_df['total_deaths'], label = 'Total de Casos {}'.format(paises))
            plt.plot(df_World['total_deaths'], label = 'Total de Casos a Nivel Mundial')
            plt.yscale("log")
            plt.title('Escala Logaritmica')
            plt.ylabel('Cantidad')
            plt.xlabel('Fechas/Mes')
            plt.grid()
            plt.legend()
            st.pyplot()
        if st.checkbox("Gráfico de Tasa de Mortalidad a Nivel Mundial y de {}".format(paises)):
            df_mort_pais = (paises_df.total_deaths / paises_df.total_cases) * 100
            # Tasas de muertes en el mundo
            df_mort_mundo = (df_World.total_deaths / df_World.total_cases) * 100
            #plt.style.use('ggplot')
            plt.plot(df_mort_pais, label = 'Tasa de mortalidad en {}'.format(paises))
            plt.plot(df_mort_mundo, label = 'Tasa de mortalidad en el Mundo')
            plt.title('Tasa de Mortalidad en {} vs Mundo (Mensual)'.format(paises))
            plt.ylabel('% de Mortalidad')
            #plt.xticks(rotation = 45)
            plt.legend()
            plt.grid()
            st.pyplot()
        #EN COMPARACION con OTROS PAISES
        st.subheader('Gráficos Comparativos de {} con Otros Paises'.format(paises))
        paises_seleccionados = df.location.unique().tolist()
        selected_columns = st.multiselect("Seleccionar los Paises a Comparar: ", paises_seleccionados)
        #st.write(selected_columns)
        if len(selected_columns) > 0:
            st.warning("ADVERTENCIA: Es recomendable seleccionar pocos paises para agilizar el procesamiento")
            if st.checkbox("Realizar los Gráficos Comparativos"):
                selected_columns.append(paises)
                df_comparacion = df[df['location'].isin(selected_columns)]
                #Tasa Mortalidad
                st.subheader("Comparativa de la Tasa de Mortalidad de COVID-19 de {}".format(paises))
                #fig, ax = plt.subplots(figsize=(14,10))
                for i in selected_columns:
                    df_mortalidad = (df_comparacion[df_comparacion['location']== i].total_deaths/df_comparacion[df_comparacion['location']== i].total_cases)*100
                    plt.plot(df_mortalidad, label = i)
                    plt.legend()
                plt.grid()
                plt.xlabel("Fechas/Mes")
                plt.ylabel("% Mortalidad [Numero Total de Muertes/Numero Total de Casos]")
                st.pyplot()
                #Total de Casos
                indice_paises = paises_df.index[-1] #El penuntilmo indice para asegurar
                st.subheader("Total de Casos y Muertes de COVID-19 de {} al {}".format(paises, indice_paises))
                df_aux = df.loc[indice_paises, ['location', 'total_cases','total_deaths','total_cases_per_million','total_deaths_per_million']]
                df_aux =  df_aux[df_aux['location'].isin(selected_columns)]
                fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,6))
                sns.barplot(df_aux.location,df_aux.total_cases, palette='Paired', ax=ax1)
                ax1.set_xlabel('Paises')
                ax1.set_ylabel('Total de Casos')
                ax1.set_title('Total de Casos al {}'.format(indice_paises))
                sns.barplot(df_aux.location,df_aux.total_deaths, palette='Paired', ax=ax2)
                ax2.set_xlabel('Paises')
                ax2.set_ylabel('Total de Muertes')
                ax2.set_title('Total de Muertes al {}'.format(indice_paises))
                plt.tight_layout()
                st.pyplot()
                st.subheader("Total de Casos y Muertes de COVID-19 por millon de habitantes de {} al {}".format(paises, indice_paises))
                fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,6))
                sns.barplot(df_aux.location,df_aux.total_cases_per_million, palette='Paired', ax=ax1)
                ax1.set_xlabel('Paises')
                ax1.set_ylabel('Total de Casos por Millon de Habitantes')
                ax1.set_title('Total de Casos/millon al {}'.format(indice_paises))
                sns.barplot(df_aux.location,df_aux.total_deaths_per_million, palette='Paired', ax=ax2)
                ax2.set_xlabel('Paises')
                ax2.set_ylabel('Total de Muertes por Millon de Habitantes')
                ax2.set_title('Total de Muertes/millon al {}'.format(indice_paises))
                plt.tight_layout()
                st.pyplot()
    
    ##NUEVO MENU: ANALISIS EXPLORATORIO Mundial
    elif add_selectbox == 'Análisis Exploratorio a Nivel Mundial':
        #Transformar la columna "date" no formato datetime
        st.header("Análisis Exploratorio a Nivel Mundial")
        df.date = pd.to_datetime(df.date)
        df.date.max()
        df.set_index('date', inplace=True)
        df_world = df[df.location=='World'] #Pega de todo el mundo
        indice = df_world.index[-1]
        st.subheader("TOP 10 Paises con Más Casos de COVID-19 al {}".format(indice))
        df_world = df[df.location=='World'] #Pega de todo el mundo
        df_aux = df.loc[indice, ['location', 'total_cases']].sort_values(by='total_cases', ascending=False)[1:11]
        fig, ax = plt.subplots(figsize=(10,6))
        ax.grid()
        sns.barplot(df_aux.location, df_aux.total_cases, palette='Paired', ax=ax)
        #ax.set_title('TOP 5 Países com mais casos de COVID-19')
        ax.set_xlabel('Países')
        ax.set_ylabel('Total de Casos')
        plt.tight_layout()
        st.pyplot()
        st.subheader("TOP 10 Paises con Más Muertes de COVID-19 al {}".format(indice))
        df_aux = df.loc[indice, ['location', 'total_deaths']].sort_values(by='total_deaths', ascending=False)[1:11]
        fig, ax = plt.subplots(figsize=(10,6))
        sns.barplot(df_aux.location, df_aux.total_deaths, palette='Paired', ax=ax)
        ax.grid()
        #ax.set_title('TOP 5 Países com mais casos de COVID-19')
        ax.set_xlabel('Países')
        ax.set_ylabel('Total de Muertes')
        plt.tight_layout()
        st.pyplot()
        st.subheader("Tasa de Mortalidad de COVID-19 del TOP 10 Paises {}".format(indice))
        df_aux = df.loc[indice, ['location', 'total_deaths','total_cases']].sort_values(by='total_deaths', ascending=False)[1:11]
        df_aux['mortalidad'] = (df_aux.total_deaths/df_aux.total_cases)*100
        fig, ax = plt.subplots(figsize=(10,6))
        sns.barplot(df_aux.location, df_aux.mortalidad, palette='Paired', ax=ax)
        #ax.set_title('TOP 5 Países com mais casos de COVID-19')
        ax.set_xlabel('Países')
        ax.set_ylabel('Tasa de Mortalidad')
        ax.grid()
        plt.tight_layout()
        st.pyplot()









if __name__ == "__main__":
    main()