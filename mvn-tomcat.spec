#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-tomcat
Version  : 5.5.23
Release  : 1
URL      : https://repo1.maven.org/maven2/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.jar
Source0  : https://repo1.maven.org/maven2/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.jar
Source1  : https://repo1.maven.org/maven2/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.pom
Source2  : https://repo1.maven.org/maven2/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.jar
Source3  : https://repo1.maven.org/maven2/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.pom
Source4  : https://repo1.maven.org/maven2/tomcat/tomcat-parent/5.5.23/tomcat-parent-5.5.23.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 CDDL-1.0 EPL-1.0
Requires: mvn-tomcat-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-tomcat package.
Group: Data

%description data
data components for the mvn-tomcat package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-compiler/5.5.23
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-compiler/5.5.23
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-runtime/5.5.23
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-runtime/5.5.23
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/tomcat/tomcat-parent/5.5.23
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/tomcat/tomcat-parent/5.5.23/tomcat-parent-5.5.23.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.jar
/usr/share/java/.m2/repository/tomcat/jasper-compiler/5.5.23/jasper-compiler-5.5.23.pom
/usr/share/java/.m2/repository/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.jar
/usr/share/java/.m2/repository/tomcat/jasper-runtime/5.5.23/jasper-runtime-5.5.23.pom
/usr/share/java/.m2/repository/tomcat/tomcat-parent/5.5.23/tomcat-parent-5.5.23.pom
