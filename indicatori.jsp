<%@page contentType="text/html" pageEncoding="windows-1252"%>

<%@ page import = "java.util.ArrayList,
                   java.util.Iterator,
                   java.util.List,
                   java.util.Map,
                   java.util.SortedMap,
                   java.util.TreeMap,
                   it.infolog.sce.model.Indicatore,
                   it.infolog.sce.core.Indicatori,
                   it.infolog.sce.framework.gui.DefaultRenderer;" %>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">

<%
/* Costruisco la mappa degli indicatori distinti per gruppo: gruppo = key */
SortedMap mappaIndicatoriPerGruppo = new TreeMap();

/* Recupero gli indicatori dell'utente web di default */
List indicatoriUtenteWeb = Indicatori.getIndicatoriUtenteWeb();

/**
 * Ciclo gli indicatori associati all'utente e popolo la mappa per gruppo a
 * seconda del gruppo settato sull'indicatore
 */
if(indicatoriUtenteWeb != null && !indicatoriUtenteWeb.isEmpty()){
  for (int i = 0; i < indicatoriUtenteWeb.size(); i++) {
    Indicatore indicatore = (Indicatore)indicatoriUtenteWeb.get(i);
    String gruppo = "";
	
	if(!indicatore.isIndicatoreAttivo()){
      continue;
    }

    if(indicatore.getGruppo() != null && indicatore.getGruppo().trim().length() > 0){
      gruppo = indicatore.getGruppo().trim();
    }

    Object listaIndicatori = mappaIndicatoriPerGruppo.get(gruppo);
    if(listaIndicatori == null){
      listaIndicatori = new ArrayList();
    }
    ((List)listaIndicatori).add(indicatore);

    mappaIndicatoriPerGruppo.put(gruppo, listaIndicatori);
  }
}
%>

<html>
  <head>
    <title>Indicatori</title>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <link href="styles/style.css" rel="stylesheet" type="text/css">
    <link href="favicon.ico" rel="shortcut icon">
  </head>
  <body class="body">
    <table width=100% cellpadding="0" cellspacing="0">
        <tr class="sfondoBanner">
            <td width="150" align="left"><img src="images/logo/logo_intellimag.png" alt="intellimag"></td>
            <td class="indicatoriTitolo" align="left">Indicatori</td>
            <td width="150" align="right"><img src="images/logo/logo_cliente.png" alt="cliente"></td>
        </tr>
        <tr>
            <td colspan="3">
                <table class="pagTabellaInd">
                    <tr>
                        <td>
                            <table class="tabellaIndicatori" cellspacing="0" cellpadding="10">
                                <%
                                /**
                                 * Ciclo sulla mappa ottenuta per gruppo
                                 */
                                Iterator it = mappaIndicatoriPerGruppo.keySet().iterator();
                                while(it.hasNext()){
                                  String chiaveGruppo = (String)it.next();
                                  List indicatoriGruppo = (List)mappaIndicatoriPerGruppo.get(chiaveGruppo);

                                  if(indicatoriGruppo == null || indicatoriGruppo.isEmpty()){
                                    continue;
                                  }

                                  Indicatore primoIndicatore = (Indicatore)indicatoriGruppo.get(0);
                                  String eticGruppo = (primoIndicatore.getEtichettaGruppo() != null &&
                                                       primoIndicatore.getEtichettaGruppo().trim().length() > 0)
                                                      ? primoIndicatore.getEtichettaGruppo().trim() : chiaveGruppo;

                                %>
                                  <tr align="center">
                                    <td colspan="3" class="tabellaIndicatoriGruppo"><%=eticGruppo%></td>
                                  </tr>
                                  <tr>
                                    <th class="tabellaIndicatori" align="left">Descrizione</th>
                                    <th class="tabellaIndicatori" align="right">Valore</th>
                                    <th class="tabellaIndicatori" align="center">UM</th>
                                  </tr>
                                <%
                                  /**
                                   * Ciclo sugli indicatori del gruppo
                                   */
                                  for(int j = 0; j < indicatoriGruppo.size(); j++){
                                    Indicatore indicatore = (Indicatore)indicatoriGruppo.get(j);
                                    String descrizione = (indicatore.getDescrizione() != null && indicatore.getDescrizione().trim().length() > 0)
                                                          ? indicatore.getDescrizione().trim() : indicatore.getCodice();

                                    String um = (indicatore.getUm() != null && indicatore.getUm().trim().length() > 0)
                                                 ? indicatore.getUm().trim() : "";

                                    /* Recupero il valore calcolato dell'indicatore */
                                    Object result = Indicatori.getMappaValoriIndicatori().get(indicatore.getCodice());
                                    String testoValue = "";
                                    
                                    Object resultClass = null;
                                    if(result != null){
                                      try{
                                        Class classe = Class.forName(indicatore.getTipoDato());
                                        resultClass = classe.cast(result);
                                        testoValue = DefaultRenderer.render(resultClass, indicatore.getFormato());
                                      }catch(Exception e){
                                        testoValue = "";
                                      }
                                    }
                                %>
                                    <tr align="center">
                                        <td class="tabellaIndicatori" align="left"><%=descrizione%></td>
                                        <td class="tabellaIndicatori" align="right"><b><%=testoValue%></b></td>
                                        <td class="tabellaIndicatori" align="center"><%=um%></td>
                                    </tr>
                                <%
                                  }
                                %>
                                  <tr align="center">
                                      <td colspan="3" class="tabellaIndicatori">&nbsp;</td>
                                  </tr>
                                <%
                                }
                                %>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr class="win_footer">
            <td colspan="3" class="pubblicita">
                <span>&nbsp;by <b>INFOLOG SPA</b> Modena</span>
            </td>
        </tr>
    </table>
  </body>
</html>
