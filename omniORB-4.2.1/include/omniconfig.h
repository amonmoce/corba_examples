/* -*- Mode: C++; -*-
 *                            Package   : omniORB
 * omniconfig.h.in            Created on: 2002/07/11
 *                            Author    : Duncan Grisby (dgrisby)
 *
 *    Copyright (C) 2002 Duncan Grisby
 *
 *    This file is part of the omniORB library
 *
 *    The omniORB library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU Library General Public
 *    License as published by the Free Software Foundation; either
 *    version 2 of the License, or (at your option) any later version.
 *
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *    Library General Public License for more details.
 *
 *    You should have received a copy of the GNU Library General Public
 *    License along with this library; if not, write to the Free
 *    Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  
 *    02111-1307, USA
 *
 *
 * Description:
 *	*** PROPRIETARY INTERFACE ***
 *
 *      omniconfig.h used when using autoconf. Nothing in this file is
 *      replaced by autoconf, but the copying of this file over the
 *      non-autoconf version selects the autoconf setup.
 */

#ifndef __omniconfig_h__
#define __omniconfig_h__

#include <omniORB4/acconfig.h>

#define __darwin__ 1
#define __x86__ 1
#define __OSVERSION__ 1

#undef PACKAGE_BUGREPORT
#undef PACKAGE_NAME
#undef PACKAGE_STRING
#undef PACKAGE_TARNAME
#undef PACKAGE_VERSION

#endif
