%{?scl:%scl_package nodejs-tar}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-tar
Version:    2.2.1
Release:    3%{?dist}
Summary:    Tar for Node.js
License:    ISC
URL:        https://github.com/isaacs/node-tar
Source0:    http://registry.npmjs.org/tar/-/tar-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A Node.js module that supports reading and writing POSIX "tar" archives.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tar
cp -pr lib tar.js package.json %{buildroot}%{nodejs_sitelib}/tar

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/tar
%doc README.md examples LICENSE

%changelog
* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.1-3
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.1-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 2.2.1-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.3-1
- New upstream release 1.0.3

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.1.19-1
- New upstream release 0.1.19

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.18-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.18-1
- new upstream release 0.1.18

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.17-2
- Add support for software collections

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.17-1
- new upstream release 0.1.17

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.16-1
- new upstream release 0.1.16

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-3
- add missing build section
- fix URL

* Sun Jan 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-2
- provide a better description and summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.14-1
- new upstream release 0.1.14
- clean up for submission

* Thu Mar 15 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- initial package
