/***************************************************************
*
* (c) 2009 Markus Dittrich 
*
* This program is free software; you can redistribute it 
* and/or modify it under the terms of the GNU General Public 
* License Version 3 as published by the Free Software Foundation. 
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License Version 3 for more details.
*
* You should have received a copy of the GNU General Public 
* License along with this program; if not, write to the Free 
* Software Foundation, Inc., 59 Temple Place - Suite 330, 
* Boston, MA 02111-1307, USA.
*
****************************************************************/

/** Qt headers */

/** local headers */
#include "basicDefs.h"
#include "knittingSymbol.h"


/**************************************************************
 *
 * PUBLIC FUNCTIONS 
 *
 **************************************************************/

//-------------------------------------------------------------
// constructor
//-------------------------------------------------------------
KnittingSymbol::KnittingSymbol(const QString& aPath,
  const QString& aName, const QSize& aDimension,
  const QString& aDescription, const QString& aInstruction)
  :
    svgPath_(aPath),
    name_(aName),
    dimensions_(aDimension),
    description_(aDescription),
    instructions_(aInstruction)
{
  status_ = SUCCESSFULLY_CONSTRUCTED;
}



//--------------------------------------------------------------
// main initialization routine
//--------------------------------------------------------------
bool KnittingSymbol::Init()
{
  if ( status_ != SUCCESSFULLY_CONSTRUCTED )
  {
    return false;
  }

  return true;
}






/* define an empty knittingSymbol object for convenience */



