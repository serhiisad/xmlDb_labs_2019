<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match = "/">
        <!--<!DOCTYPE html>-->
        <html>
            <head>
                <title>Tennis Shoes</title>
            </head>

            <body>
                <h2>Tennis shoes</h2>
                <table border="1">
                <tr bgcolor="#9acd32">
                  <th>Image</th>
                  <th>Description</th>
                  <th> Price</th>
                 </tr>
                <xsl:for-each select="items/item">
                <tr>
                  <td>
                      <!--<img  width="100" height="100">-->
                        <!--<xsl:attribute name="src">-->
                           <!--<xsl:value-of select="image_urls"/>-->
                        <!--</xsl:attribute>-->
                      <!--</img>-->
                      <!--<xsl:value-of select="image_urls"/>-->
                      <img src="{image_urls}" width="100" height="100" alt="No image"></img>
                  </td>
                  <td>
                      <xsl:value-of select="title"/>
                  </td>
                  <td>
                      <xsl:value-of select="price"/>
                  </td>
                </tr>
                </xsl:for-each>
              </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>