/***************************************************************
*
* (c) 2009-2010 Markus Dittrich
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

#ifndef GRAPHICS_SCENE_H
#define GRAPHICS_SCENE_H

/* boost includes */
#include <boost/shared_ptr.hpp>
#include <boost/utility.hpp>

/* QT includes */
#include <QColor>
#include <QGraphicsScene>
#include <QPair>
#include <QList>
#include <QMap>

/* local includes */
#include "knittingSymbol.h"
#include "io.h"


QT_BEGIN_NAMESPACE


/* a few forward declarations */
class LegendItem;
class LegendLabel;
class KnittingPatternItem;
class PatternGridItem;
class PatternGridRectangle;
class QGraphicsSceneMouseEvent;
class QKeyEvent;
class QSettings;
class MainWindow;


namespace
{
/* convenience constants */
const int UNSELECTED = -100;
const int NOSHIFT    = -101;

/* convenience typedefs */
typedef QList<QPair<int, int> > RowLayout;
typedef QList<PatternGridItem*> RowItems;
typedef QPair<LegendItem*, LegendLabel*> LegendEntry;
};



/****************************************************************
 *
 * definitions of copy object
 *
 ***************************************************************/
struct CopyObjectItem {
  KnittingSymbolPtr symbol;
  QColor backColor;
  QSize size;
  int row;
  int column;
};
typedef boost::shared_ptr<CopyObjectItem> CopyObjectItemPtr;


struct CopyObject {
  QList<CopyObjectItemPtr> objects;
  int width;    // width of copy object in columns
  int height;   // height of copy object in rows
};




/***************************************************************
 *
 * The GraphicsScene handles the sconcho's main drawing
 * canvas
 *
 ***************************************************************/
class GraphicsScene
    :
    public QGraphicsScene,
    public boost::noncopyable
{

  Q_OBJECT



public:

  explicit GraphicsScene( const QPoint& origin, const QSize& gridsize,
                          const QSettings& settings,
                          KnittingSymbolPtr defaultSymbol,
                          MainWindow* myParent = 0 );
  bool Init();

  /* helper functions */
  void select_region( const QRectF& region );
  void reset_grid( const QSize& newSize );
  void load_new_canvas(
    const QList<PatternGridItemDescriptorPtr>& newItems );
  void instantiate_legend_items(
    const QList<LegendEntryDescriptorPtr>& newExtraLegendItems );
  void place_legend_items(
    const QList<LegendEntryDescriptorPtr>& newLegendEntries );
  QRectF get_visible_area() const;
  QPoint get_grid_center() const;

  /* legend releated stuff */
  bool legend_is_visible() const { return legendIsVisible_; }
  void hide_all_but_legend();
  void show_all_items();
  QMap<QString, LegendEntry> get_legend_entries() const {
    return legendEntries_;
  }


signals:

  void mouse_moved( QPointF position );
  void statusBar_error( QString msg );
  void statusBar_message( QString msg );
  void show_whole_scene();
  void grabbed_color( const QColor& aColor );


public slots:

  void update_selected_symbol( const KnittingSymbolPtr symbol );
  void add_symbol_to_legend( const KnittingSymbolPtr symbol );
  void grid_item_selected( PatternGridItem* item, bool status );
  void grid_item_reset( PatternGridItem* item );
  void update_selected_background_color( const QColor& aColor );
  void deselect_all_active_items();
  void mark_active_cells_with_rectangle();
  void update_after_settings_change();
  void toggle_legend_visibility();
  void load_settings();


protected:

  void mousePressEvent( QGraphicsSceneMouseEvent* mouseEvent );
  void mouseMoveEvent( QGraphicsSceneMouseEvent* mouseEvent );


private slots:

  void open_row_col_menu_();
  void insert_rows_( int numRows, int pivotRow, int direction );
  void delete_row_( int row );
  void insert_columns_( int numCols, int pivotCol, int direction );
  void delete_column_( int col );
  void mark_rectangle_for_deletion_( QObject* foo );
  void customize_rectangle_( QObject* foo );
  void update_key_label_text_( QString, QString );
  void copy_items_();
  void paste_items_();
  void grab_color_();
  void notify_legend_of_item_addition_( const KnittingSymbolPtr symbol,
                                        QColor color, QString extraTag );
  void notify_legend_of_item_removal_( const KnittingSymbolPtr symbol,
                                       QColor color, QString extraTag );


private:

  /* construction status variable */
  int status_;

  /* do we want active items to be updated */
  bool updateActiveItems_;

  /* basic dimensions */
  QPoint origin_;
  int numCols_;
  int numRows_;
  QSize gridCellDimensions_;
  QFont textFont_;


  /* holds the index of the currently selected column/row if any */
  int selectedCol_;
  int selectedRow_;

  /* reference to settings */
  const QSettings& settings_;

  /* list of currenly selected items */
  QMap<int, PatternGridItem*> activeItems_;

  /* currently copied selection */
  CopyObject copiedItems_;

  /* pointers to current user selections (knitting symbol,
   * color, pen size ..) */
  KnittingSymbolPtr selectedSymbol_;
  KnittingSymbolPtr defaultSymbol_;
  QColor backgroundColor_;
  QColor defaultColor_;

  /* set up functions for canvas */
  void create_pattern_grid_();
  void create_grid_labels_();
  void create_pattern_key_();

  /* items related to the legend */
  bool legendIsVisible_;
  void shift_legend_items_vertically_( int pivot, int globalOffset,
                                       int localOffset = 0 );
  void shift_legend_items_horizontally_( int pivot, int globalOffset );
  void update_legend_labels_();
  int get_next_legend_items_y_position_() const;
  QList<QGraphicsItem*> get_all_legend_items_() const;
  QList<QGraphicsItem*> get_all_svg_legend_items_() const;
  QList<QGraphicsItem*> get_all_text_legend_items_() const;


  /* List of items in the current Legend */
  QMap<QString, LegendEntry> legendEntries_;

  /* map holding the descriptor for all currently "known"
   * knitting symbols (even ones not currently shown, e.g.
   * for symbols that were previously visible, had their
   * text changed and then disappered again since the user
   * removed all instances of the symbol from the pattern) */
  QMap<QString, QString> symbolDescriptors_;
  QString get_symbol_description_( KnittingSymbolPtr aSymbol,
                                   QString aColorName );

  /* reference count of knitting symbols currently in use */
  QMap<QString, int> usedKnittingSymbols_;

  /* use these to add/remove PatternGridItems to the scene */
  void add_patternGridItem_( PatternGridItem* anItem );
  void remove_patternGridItem_( PatternGridItem* anItem );

  /* these functions take care of resetting the canvas */
  void reset_canvas_();
  void purge_all_canvas_items_();
  void purge_legend_();

  /* helper functions */
  void try_place_knitting_symbol_();
  void change_selected_cells_colors_();

  void colorize_highlighted_cells_();
  QPair<int, int> get_cell_coords_( const QPointF& mousePosition ) const;
  int compute_horizontal_label_shift_( int num, int fontSize ) const;
  bool sort_active_items_row_wise_( QList<RowItems>& rows ) const;
  bool process_selected_items_( QList<RowLayout>& processedCellLayout,
                                const QList<RowItems>& rowSelection,
                                int targetPatternSize );

  void select_column_( int col );
  void select_row_( int row );
  void insert_single_column_( int col );
  void insert_single_row_( int row );
  void expand_grid_( int colStart, int rowStart );

  void enable_canvas_update_() { updateActiveItems_ = true; }
  void disable_canvas_update_() { updateActiveItems_ = false; }
  void update_active_items_();

  QPoint compute_cell_origin_( int col, int row ) const;
  int compute_cell_index_( PatternGridItem* anItem ) const;
  QPair<int, int> compute_from_cell_index_( int index ) const;

  PatternGridItem* patternGridItem_at_( int col, int row ) const;

  bool handle_click_on_marker_rectangle_(
    const QGraphicsSceneMouseEvent* mouseEvent );
  void show_rectangle_manage_menu_( PatternGridRectangle* aRect,
                                    const QPoint& pos );

  bool handle_click_on_grid_array_(
    const QGraphicsSceneMouseEvent* mouseEvent );
  bool handle_click_on_grid_labels_(
    const QGraphicsSceneMouseEvent* mouseEvent );

  QPair<bool, int> is_row_contiguous_( const RowItems& items ) const;
  QRect find_bounding_rectangle_( const QList<RowItems>& rows ) const;
};


QT_BEGIN_NAMESPACE

#endif
