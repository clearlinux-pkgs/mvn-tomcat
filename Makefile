PKG_NAME := mvn-tomcat
URL = https://repo1.maven.org/maven2/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.jar
ARCHIVES = https://repo1.maven.org/maven2/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.pom : https://repo1.maven.org/maven2/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.jar : https://repo1.maven.org/maven2/tomcat/tomcat-parent/5.5.23/tomcat-parent-5.5.23.pom : https://repo1.maven.org/maven2/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.pom :

include ../common/Makefile.common
